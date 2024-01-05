# ROS Imports
import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from rclpy.action.client import ActionClient
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup
from rclpy.executors import MultiThreadedExecutor
from std_msgs.msg import String 

# Create3 Packages
import irobot_create_msgs
from irobot_create_msgs.action import DriveDistance, Undock, RotateAngle, NavigateToPosition, AudioNoteSequence
from geometry_msgs.msg import PoseStamped
from irobot_create_msgs.srv import ResetPose
from irobot_create_msgs.msg import AudioNoteVector, AudioNote
from builtin_interfaces.msg import Duration

# key_commander stuff
from pynput.keyboard import KeyCode
from key_commander import KeyCommander
# Python Packages
import random, time
from math import pi
from collections import deque

# These AudioNote objects are encapsulated within lists to form AudioNoteVector instances when used with the chirp method.
# The frequency parameter in AudioNote determines the pitch of the tone, while max_runtime specifies its duration.
# Different sequences of notes can be created and used to convey specific messages or statuses through sound.
start_note = [ AudioNote(frequency=600, max_runtime=Duration(sec=0, nanosec= 50000000))]
end_note =   [ AudioNote(frequency=784, max_runtime=Duration(sec=0, nanosec= 50000000))]
rand_note =  [ AudioNote(frequency=350, max_runtime=Duration(sec=0, nanosec= 150000000))]
ready_notes = [
	AudioNote(frequency=583, max_runtime=Duration(sec=0, nanosec= 50000000)),
	AudioNote(frequency=784, max_runtime=Duration(sec=0, nanosec=100000000))
]
error_notes = [
	AudioNote(frequency=583, max_runtime=Duration(sec=0, nanosec= 50000000)),
	AudioNote(frequency=350, max_runtime=Duration(sec=0, nanosec=100000000))
]

# Node Imports
from dock_status_node import DockStatusMonitorNode
from ir_status_node import IrMonitorNode
from odometry_node import OdomNode

# Initialize and connect to other nodes
rclpy.init()
namespace = 'create3_0561'
dock_sensor = DockStatusMonitorNode(namespace)
ir_sensor = IrMonitorNode(namespace)
odometry_sensor = OdomNode(namespace)

class Roomba(Node):
    def __init__(self, namespace):
        super().__init__('roomba_node')
        # Initializing individual sensors as node objects for operational purposes
        self.dock_sensor = dock_sensor
        self.ir_sensor = ir_sensor
        self.odometry_sensor = odometry_sensor

        # Creating callback groups for managing subscription callbacks
        # This helps in handling multiple asynchronous events without interference.
        # NOTE: These are probably not needed anymore since I split their purposes into their own individual nodes.
        """
		The MutuallyExclusiveCallbackGroup() ensures that callbacks within this group 
		do not run at the same time, preventing conflicts and managing resource access 
		effectively. In the Roomba node, this group is used to organize callbacks for 
		dock status, IR sensor data, and pose information, allowing controlled execution 
		and better handling of shared resources.
		"""
        cb_dockstatus = MutuallyExclusiveCallbackGroup()
        cb_ir = MutuallyExclusiveCallbackGroup()
        cb_pose = MutuallyExclusiveCallbackGroup()

        # Subscriptions
        self.dock_status_sub_ = self.create_subscription(String, f'/{namespace}/check_dock_status', 
                                                self.dock_status_callback, 10, callback_group=cb_dockstatus)
        self.ir_opcode_sub_ = self.create_subscription(String, f'/{namespace}/ir_opcode_number', 
                                                self.ir_opcode_callback, qos_profile_sensor_data, callback_group=cb_ir)
        self.current_pose_sub_ = self.create_subscription(PoseStamped, f'/{namespace}/pose_stamped', 
                                                self.pose_callback, qos_profile_sensor_data, callback_group=cb_pose)

		# Actions: Made a thread just for chirps since they are often used just after or before an action
        cb_Action = MutuallyExclusiveCallbackGroup()
        cb_chirp  = MutuallyExclusiveCallbackGroup()

        # These are all the actions the script uses within later methods.
        """
        Action clients are assigned to a callback group (cb_Action or cb_chirp), which manages
        their execution. The cb_Action group is likely used for actions related to movement 
        and navigation, ensuring their sequential execution and avoiding conflicts. The 
        cb_chirp group, separates these less critical actions from the movement-related ones, 
        allowing for independent management and potentially verlapping execution with non-conflicting actions.
        """
        self.undock_ac = ActionClient(self, Undock, f'/{namespace}/undock', callback_group=cb_Action)
        self.drive_ac = ActionClient(self, DriveDistance, f'/{namespace}/drive_distance', callback_group=cb_Action)
        self.nav_to_pos_ac = ActionClient(self, NavigateToPosition, f'/{namespace}/navigate_to_position', callback_group=cb_Action)
        self.audio_ac = ActionClient(self, AudioNoteSequence, f'/{namespace}/audio_note_sequence', callback_group=cb_chirp)
        self.rotate_ac = ActionClient(self, RotateAngle, f'/{namespace}/rotate_angle', callback_group=cb_Action)
        
        # Initializing the ResetPose service client
        # This service is used to reset the robot's pose estimate, crucial after undocking.
        self.reset_pose_srv = self.create_client(ResetPose, f'/{namespace}/reset_pose')
        while not self.reset_pose_srv.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('ResetPose service not available, waiting again...')

        # Initializing variables to store data received from other nodes
        # These variables are updated in the callback functions.
        self.latest_dock_status = None
        self.latest_pose_stamped = None
        self.latest_ir_opcode = None
        self.ir_opcode_history = deque(maxlen=20)  # A deque to store the history of IR opcodes for decision making in docking.

    def dock_status_callback(self, msg):
        # Update the latest dock status with the message received from the subscribed topic
        # Logs the received status for debugging and monitoring purposes
        self.latest_dock_status = msg.data
        self.get_logger().info(f"Received /is_docked status: {self.latest_dock_status}")

    def pose_callback(self, msg):
        # Update the latest pose stamped data with the message received from the subscribed topic
        # This data is crucial for navigation tasks
        self.latest_pose_stamped = msg
        self.get_logger().info(f"Received stamped pose status: {self.latest_pose_stamped}")

    def ir_opcode_callback(self, msg):
        # Update the latest IR opcode with the message received from the subscribed topic
        # Logs the received opcode and its data type for debugging and confirmation
        self.latest_ir_opcode = msg
        print("msg", msg)
        print(type(msg))
        print("msg.data:", self.latest_ir_opcode)
        print("DEBUG: All opcode information:", msg)
        self.get_logger().info(f"Received IrOpcode: {self.latest_ir_opcode}")

    def chirp(self, sent_notes):
        """
        This method uses the audio_ac action client to play a series of audio notes on the robot.

        The AudioNoteSequence action defines the structure for audio playback requests.
        sent_notes: A list of AudioNote objects, each specifying a note to be played.

        The method performs the following steps:
        1. Waits for the audio action server to be ready, ensuring that the request can be processed.
        2. Creates an AudioNoteSequence goal with the desired specifications for the note sequence.
        3. Sets goal.iterations to 1, indicating that the note sequence should be played once.
        4. Constructs an AudioNoteVector from the sent_notes, which is a sequence of AudioNote objects.
        Each AudioNote in the sequence has its own frequency and duration, defining the specific sound to be played.
        5. Sends the goal to the audio action server asynchronously. The server then processes the request and plays the specified sequence of notes.

        This function is primarily used to provide auditory feedback or signals during various robot operations.
        For example, it can signal the start or end of an action, alert about a state change, or provide confirmatory beeps.
        """
        # Wait for the audio action server to be ready
        self.audio_ac.wait_for_server()
        goal = AudioNoteSequence.Goal()
        goal.iterations = 1
        goal.note_sequence = AudioNoteVector(notes=sent_notes)
        # Send the goal to play the specified notes
        self.audio_ac.send_goal_async(goal)

    def undock(self):
        # Method to undock the robot, involves playing a chirp, checking dock status, and sending an undock command
        self.chirp(start_note)
        # Publish the current dock status and wait for the undock action server to be ready
        self.dock_sensor.publish_dock_status()
        self.undock_ac.wait_for_server()
        undock_goal = Undock.Goal()
        # Send the undock goal to the action server
        self.undock_ac.send_goal(undock_goal)
        self.dock_sensor.publish_dock_status()
        time.sleep(1)
        self.chirp(end_note)

    def reset_pose(self):
        """
        This method is responsible for resetting the robot's pose estimate. This is done
        right after undocking, and is followed by recording the pose using PoseStamped.


        Steps performed in this method:
        1. A request object for the ResetPose service is created. This request doesn't 
        require any specific parameters as it simply resets the robot's internal pose 
        estimate.
        2. The ResetPose service is called asynchronously. This means the request is sent 
        to the service, and the method doesn't wait for the response to continue its 
        execution. This is useful in scenarios where the response time might vary, or 
        the service call shouldn't block other processes.
        3. If the response from the service is not None, it indicates that the service 
        call was successfully received and likely processed by the server. In such a 
        case, a log message is recorded for successful service invocation.
        4. If the response is None, it suggests that there was no response from the 
        ResetPose service, possibly due to issues like the service not being available 
        or not responding in time. An error log is recorded in this case.
        5. The method is wrapped in a try-except block to handle any exceptions that 
        might occur during the service call. This could include communication errors, 
        issues with the service server, or other unexpected problems. Any caught 
        exceptions are logged as errors.
        """
        try:
            request = ResetPose.Request()
            # Call the ResetPose service asynchronously
            response = self.reset_pose_srv.call_async(request)
            if response is not None:
                self.get_logger().info('ResetPose service called successfully.')
                time.sleep(1)
            else:
                self.get_logger().error('No response from ResetPose service.')
        except Exception as e:
            self.get_logger().error(f'Failed to call ResetPose service: {e}')

    def record_pose(self):
        """
        This method stores the robot's current pose for future reference. This storage 
        is particularly useful when the robot is returning to its dock.

        The method performs the following steps:
        1. It requests the odometry sensor to publish the current odometry data. This 
        is crucial for getting the most recent position and orientation of the robot.
        2. A short delay (1 second) is introduced after the odometry publication 
        request to make sure it has been updated.
        3. Checks if the latest pose (latest_pose_stamped) is available. 
        If available, this pose is stored in self.recorded_pose for future use.
        4. If the latest pose is not available, an error log is recorded

        This function is called immediately after reset_pose() after the undocing action 
        robot's operation. The reset_pose() function recalibrates the robot's internal 
        pose estimate, and record_pose() captures this updated estimate. The recorded 
        pose is used to guide the robot back to a vicinity close to the docking station 
        after completing its tasks or movements. The final precise adjustments for 
        docking are handled by the docking function, which relies on fine sensor inputs 
        to accurately align and dock the robot.
        """
        # Request the odometry sensor to publish the current odometry
        odometry_sensor.publish_odometry()
        time.sleep(1)  # Short delay to ensure the odometry data is updated
        # Check if the latest pose is available and store it
        if self.latest_pose_stamped is not None:
            self.recorded_pose = self.latest_pose_stamped
            self.get_logger().info("PoseStamped recorded.")
        else:
            self.get_logger().error("No current pose available to record.")

    def drive_amnt(self, distance):
        """
        Drives the robot a specified distance.
        Synchronous method that waits for the drive action to complete.
        """
        print("Driving amount:", distance, "m")
        self.chirp(start_note)
        # Wait for the drive action server to be ready
        self.drive_ac.wait_for_server()
        # Set up the drive goal with the specified distance
        drive_goal = DriveDistance.Goal()
        drive_goal.distance = distance
        # Send the drive goal and wait for completion
        self.drive_ac.send_goal(drive_goal)
        time.sleep(1)  # Short delay for action execution
        self.chirp(end_note)

    def drive_amnt_async(self, distance):
        """
        Asynchronously drives the robot a specified distance.
        The method returns immediately after sending the goal.
        """
        print("Driving amount:", distance, "m")
        self.chirp(start_note)
        self.drive_ac.wait_for_server()
        drive_goal = DriveDistance.Goal()
        drive_goal.distance = distance
        # Send the drive goal asynchronously
        self.drive_ac.send_goal_async(drive_goal)
        time.sleep(2)  # Short delay for action initiation
        self.chirp(end_note)

    def rotate_amnt(self, angle):
        """
        Rotates the robot by a specified angle.
        Synchronous method that waits for the rotate action to complete.
        """
        print("Rotating amount:", angle, "rad")
        self.chirp(start_note)
        self.rotate_ac.wait_for_server()
        rotate_goal = RotateAngle.Goal()
        rotate_goal.angle = angle
        # Send the rotate goal and wait for completion
        self.rotate_ac.send_goal(rotate_goal)
        time.sleep(1)  # Short delay for action execution
        self.chirp(end_note)

    def rotate_amnt_async(self, angle):
        """
        Asynchronously rotates the robot by a specified angle.
        The method returns immediately after sending the goal.
        """
        print("Rotating amount:", angle, "rad")
        self.chirp(start_note)
        self.rotate_ac.wait_for_server()
        rotate_goal = RotateAngle.Goal()
        rotate_goal.angle = angle
        # Send the rotate goal asynchronously
        self.rotate_ac.send_goal_async(rotate_goal)
        time.sleep(2)  # Short delay for action initiation
        self.chirp(end_note)

    def navigate_to_recorded_pose(self):
        """
        This method navigates the robot back to a pose that was previously recorded. 
        Returns the robot to the place right after undocking by using odometry data
        for navigation.

        The method performs the following steps:
        1. Plays a start note using the chirp function to indicate the initiation of 
        navigation.
        2. Checks if a pose (self.recorded_pose) has been previously recorded. The 
        recorded pose is obtained from odometry data, which tracks the robot's 
        movement and orientation.
        3. If a pose has been recorded, it sets up a navigation goal using the 
        NavigateToPosition action. The goal includes:
        - The recorded pose, which is a PoseStamped message from the OdomNode. 
            This node is responsible for processing and publishing odometry 
            information from the /odom topic.
        - The achieve_goal_heading flag set to True to ensure the robot faces the 
            same direction upon reaching the destination.
        - Maximum translation (linear movement) and rotation (angular movement) 
            speeds are set for fun
        4. Sends the navigation goal to the action server and plays ready notes to 
        indicate the robot is in the process of navigating to the recorded pose.
        5. If no pose has been recorded, it plays error notes and logs an error 
        message. It is a depressing sound, and one that I still hear as I lie awake 
        in bed.

        The robot's ability to navigate using this method relies on accurate odometry 
        data, which is typically gathered from sensors like wheel encoders and 
        optical flow sensors. These sensors provide detailed information about the
        robot's movement and rotation, enabling precise tracking of its position and 
        orientation over time.
        """
        self.chirp(start_note)
        print("Navigating back to home position from Odometry reading (PoseStamped)")
        # Check if a pose has been previously recorded
        if self.recorded_pose is not None:
            # Set up the navigation goal with the recorded pose
            goal_msg = NavigateToPosition.Goal()
            goal_msg.goal_pose = self.recorded_pose
            goal_msg.achieve_goal_heading = True  # Ensure the robot is facing the correct direction
            goal_msg.max_translation_speed = 0.3  # Set max translation speed
            goal_msg.max_rotation_speed = 1.9  # Set max rotation speed

            # Send the navigation goal to the action server
            self.nav_to_pos_ac.wait_for_server()
            self.nav_to_pos_ac.send_goal(goal_msg)
            self.chirp(ready_notes)
        else:
            # Play error notes and log if no pose has been recorded
            self.chirp(error_notes)
            self.get_logger().error("No pose has been recorded.")

    def docking(self):
        """
        Executes the docking process for the robot using infrared (IR) opcode-based navigation.

        This method continuously checks the robot's docking status and IR opcodes to
        navigate and align the robot with the docking station. It uses a combination of
        rotation and forward movement commands based on the received IR opcodes to
        correctly position the robot for docking.

        The robot responds to specific IR opcodes as follows:
        - Opcode 160 or 161: The robot is likely facing an obstacle or is misaligned.
        These opcodes are added to a history to detect if the robot is stuck for 20
        consecutive readings of opcode 160 or 161
        - Opcode 168: Indicates the robot should rotate slightly to the right.
        - Opcode 164: Indicates the robot should rotate slightly to the left.
        - Opcode 172: Suggests the robot is aligned and should move forward slightly.

        If the robot consistently receives opcodes 160 or 161, indicating it might be stuck,
        it will perform a backward movement to reposition itself before attempting to dock again.

        The method includes exception handling to gracefully handle unexpected errors and 
        uses sleep calls to manage the command rate, ensuring the robot has enough time
        to respond to each command.

        I noticed that the synchronous commands would stall the code here, so I moved to 
        asynchronous actions and played with the sleep timers until it worked. Without
        delays, the robot would get overloaded with commands and would just beep until
        I reset it.

        Loop Break Condition:
        The loop continues until the robot's `latest_dock_status` is 'True', which 
        indicates successful docking. The dock status is updated everywhere so that the 
        robot doesn't move anymore after actually hitting the dock. An exception or 
        successful docking will break the loop.

        Print statements throughout help monitor the code, althought it is a bit messy
        as-is. I just needed something to work.

        """

        while self.latest_dock_status != 'True':  # Continue until docked
            try:
                # Update dock status and read the latest IR opcode
                self.dock_sensor.publish_dock_status()
                self.latest_ir_opcode = self.ir_sensor.publish_ir_opcode()

                # Log the opcode and dock status for monitoring
                print("Dock function IrOpcode readout:", self.latest_ir_opcode)
                print("Start- latest_dock_status:", self.latest_dock_status)

                # Process the opcode for navigation decisions
                if self.latest_ir_opcode is not None:
                    if self.latest_ir_opcode == 160 or self.latest_ir_opcode == 161:
                        # Continue the loop upon seeing specific opcodes
                        self.ir_opcode_history.append(self.latest_ir_opcode)
                        self.get_logger().info(f"IR Opcode {self.latest_ir_opcode} seen, reiterating.")

                    elif self.latest_ir_opcode == 168:
                        # Rotate right slightly for Red Buoy detection
                        self.rotate_amnt_async(pi/36)
                        time.sleep(0.2)
                        self.get_logger().info("Rotating right slightly due to Red Buoy detection.")

                    elif self.latest_ir_opcode == 164:
                        # Rotate left slightly for Green Buoy detection
                        self.rotate_amnt_async(-pi/36)
                        time.sleep(0.2)
                        self.get_logger().info("Rotating left slightly due to Green Buoy detection.")

                    elif self.latest_ir_opcode == 172:
                        # Drive forward a small amount for both Red and Green Buoy detection
                        self.drive_amnt_async(0.01)
                        time.sleep(0.2)
                        self.get_logger().info("Driving forward due to both Red and Green Buoy detection.")

                    # Handle the case where the robot might be stuck
                    if len(self.ir_opcode_history) == self.ir_opcode_history.maxlen:
                        # Back up and navigate to the recorded pose to reattempt docking
                        self.drive_amnt(-0.3)
                        self.navigate_to_recorded_pose()
                        self.get_logger().info("Backing up due to continuous 160 or 161 opcodes.")

                    self.dock_sensor.publish_dock_status()

                time.sleep(0.3)  # Short delay for loop throttling
            except Exception as e:
                self.get_logger().error(f'Error in docking loop: {e}')
                break  # Exit the loop in case of an error

def takeoff(self):
    """
    Orchestrates a series of actions to 'take off' or start the robot's operation.
    Includes undocking, resetting pose, random rotation, NavigateToPosition and driving actions.
    At this time I can't remember why there are extra sleep timers. Would love to learn
    how to actually do this.
    """
    try:
        # Start by undocking the robot
        self.undock()
        # Reset the robot's internal pose estimate
        self.reset_pose()
        # Record the current pose for future navigation
        self.record_pose()
        time.sleep(1)
        # Drive a specified distance forward
        self.drive_amnt(0.5)
        time.sleep(1)
        # Rotate a random angle between -pi and pi
        random_angle = random.uniform(-pi, pi)
        self.rotate_amnt(random_angle)
        time.sleep(1)
        # Drive forward again
        self.drive_amnt(0.5)
        # Navigate back to the recorded pose
        self.navigate_to_recorded_pose()
        # Rotate 180 degrees
        self.rotate_amnt(pi)
        # Initiate docking process
        self.docking()
    except Exception as error:
        # Play error notes and log the error if an exception occurs
        roomba.chirp(error_notes)
        self.get_logger().error(f"Error in takeoff: {error}")

# Main execution block
if __name__ == '__main__':
    # Initialize the main Roomba node and other sensor nodes
    roomba = Roomba(namespace)
    exec = MultiThreadedExecutor(8) # Gave my VM 4 CPUs with 2 threads each
    # Add nodes to the executor for concurrent processing
    exec.add_node(roomba)
    exec.add_node(dock_sensor)
    exec.add_node(ir_sensor)
    exec.add_node(odometry_sensor)

    time.sleep(0.1)
    # Play ready notes indicating system is ready
    roomba.chirp(ready_notes)

    # Set up a KeyCommander for manual control, binding 'U' key to takeoff function
    keycom = KeyCommander([
        (KeyCode(char='u'), roomba.takeoff),
    ])
    print(" Press 'U' to initiate launch")

    try:
        # Spin the executor to handle callbacks from the added nodes
        exec.spin()
    except KeyboardInterrupt:
        # Handle keyboard interrupt for graceful shutdown
        print("KeyboardInterrupt, shutting down.")
    except Exception as error:
        # Log any unexpected errors
        print(f"Unexpected error: {error}")
    finally:
        # Shutdown the executor and destroy nodes on exiting
        exec.shutdown()
        roomba.destroy_node()
        rclpy.try_shutdown()
