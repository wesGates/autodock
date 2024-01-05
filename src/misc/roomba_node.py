# ROS Imports
import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from rclpy.qos import QoSProfile, ReliabilityPolicy

from rclpy.action.client import ActionClient
from rclpy.action.client import GoalStatus
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup
from action_msgs.msg import GoalStatus
from std_msgs.msg import Header, String, Int32, Float32, UInt8, Int16 # Some topics have specific datatypes (POTENTIALLY USELESS!!!)


# Create3 Packages
import irobot_create_msgs
from irobot_create_msgs.action import DriveDistance, Undock, RotateAngle, Dock, NavigateToPosition, AudioNoteSequence
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry  # Import Odometry
from irobot_create_msgs.srv import ResetPose
from irobot_create_msgs.msg import HazardDetectionVector, AudioNoteVector, AudioNote, IrIntensityVector, IrOpcode
from builtin_interfaces.msg import Duration

# key_commander stuff
from pynput.keyboard import KeyCode
from key_commander import KeyCommander

# Python Packages
import random, time
from math import pi

# Threading
from rclpy.executors import MultiThreadedExecutor
from threading import RLock

# Node Imports
from dock_status_node import DockStatusMonitorNode
from ir_status_node import IrMonitorNode

# Globals
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


# Initialize and connect to other nodes
rclpy.init()
namespace = 'create3_0561'
dock_sensor = DockStatusMonitorNode(namespace)
ir_sensor = IrMonitorNode(namespace)

class Roomba(Node):
	def __init__(self, namespace):
		super().__init__('roomba_node')
		self.dock_sensor = dock_sensor
		self.ir_sensor = ir_sensor

		# Subscriptions: 
		# Split up to compensate for noisy subscriptions
		cb_dockstatus = MutuallyExclusiveCallbackGroup() # Perhaps unneeded since the dock_status_node takes care of the dockstatus
		cb_ir = MutuallyExclusiveCallbackGroup()
		cb_pose = MutuallyExclusiveCallbackGroup()

		self.dock_status_sub_ = self.create_subscription(String, f'/{namespace}/check_dock_status', self.dock_status_callback, 10, 
												   callback_group=cb_dockstatus)
		# self.ir_opcode_sub_ = self.create_subscription(IrOpcode, f'/{namespace}/ir_opcode', self.ir_listener, qos_profile_sensor_data, 
		# 										callback_group=cb_ir)


		self.current_pose_sub_ = self.create_subscription(PoseStamped, f'/{namespace}/pose_stamped', self.pose_callback, qos_profile_sensor_data,
												callback_group=cb_pose)
		

		# self.current_pose = self.create_subscription(Odometry,f'/{namespace}/odom', self.odometry_callback, qos_profile_sensor_data, 
		# 									   	callback_group=cb_pose)
		# self.ir_intensity_ = self.create_subscription(IrIntensityVector, f'/{namespace}/ir_intensity', self.ir_listener, 10, 
		# 										callback_group=cb_subgroup_ir)

		# Actions:
		cb_Action = MutuallyExclusiveCallbackGroup()
		cb_chirp  = MutuallyExclusiveCallbackGroup()

		self.undock_ac = ActionClient(self, Undock, f'/{namespace}/undock',
								 			callback_group=cb_Action)
		self.drive_ac = ActionClient(self, DriveDistance, f'/{namespace}/drive_distance', 
							   				callback_group=cb_Action)
		self.nav_to_pos_ac = ActionClient(self, NavigateToPosition, f'/{namespace}/navigate_to_position', 
											callback_group=cb_Action)
		self.audio_ac = ActionClient(self, AudioNoteSequence, f'/{namespace}/audio_note_sequence', 
											callback_group=cb_chirp)
		self.rotate_ac = ActionClient(self, RotateAngle, f'/{namespace}/rotate_angle', 
											callback_group=cb_Action)
		
		# Services:
		# ResetPose service client and initialize PoseStamped variable for position reset using odometry
		self.reset_pose_srv = self.create_client(ResetPose, f'/{namespace}/reset_pose')
		# Ensure service is available
		while not self.reset_pose_srv.wait_for_service(timeout_sec=1.0):
			self.get_logger().info('ResetPose service not available, waiting again...')

		# ##################
		self.req = ResetPose.Request() 

		# ## Then,,, to capture a location:
		# self.reset_pose_srv.call(self.req) # Reset to zero (odom)
		# self.pose = PoseStamped()

		# # Next, whenever I need to call
		# nav_pos = NavigateToPosition.Goal()
		# nav_pos.goal_pose = self.pose
		# self.nav_to_pos_ac.send_goal(nav_pos) # Could copy for a nav goal nav_to_.send
		# ###########################

		# # Variable Initialization
		# self.recorded_pose = None
		self.latest_pose_stamped = None
	 


	###### Callbacks for the subscriptions ######
	def dock_status_callback(self, msg):
		dock_status = msg.data
		self.get_logger().info(f"Received /is_docked status: {dock_status}")

	# def ir_listener(self, msg_2):
	# 	pass
	# 	for i in msg_2.readings:
	# 		print('IR Intensity: ', i.header.frame_id, ' ', i.value)

	def pose_callback(self, pose_stamped_msg):
		"""
		Callback for PoseStamped messages.
		"""
		self.latest_pose_stamped = pose_stamped_msg
		# print("Pose Callback has pose_stamped_msg:", pose_stamped_msg)
		print("Pose Callback has pose_stamped_msg:", pose_stamped_msg)

		self.get_logger().info('Received PoseStamped message.')
	

	# def pose_callback(self, msg):
	# 	"""
	# 	Callback to update the current pose of the robot.
	# 	"""
	# 	if isinstance(msg, PoseStamped):
	# 		self.current_pose = msg
	# 		self.get_logger().info("Current pose updated.")
	# 	else:
	# 		self.get_logger().error("Received message is not a PoseStamped.")



	def chirp(self, sent_notes):
		"""
		This function plays a given chirp tone.
		"""
		self.audio_ac.wait_for_server()

		goal = AudioNoteSequence.Goal()
		goal.iterations = 1
		goal.note_sequence = AudioNoteVector(notes=sent_notes)  # Wrap the notes in an AudioNoteVector

		# Send the goal
		self.audio_ac.send_goal_async(goal)



	##### Methods for initial movements #####
	def undock(self):
		self.chirp(start_note)

		# Read current dock status, then undock
		self.dock_sensor.publish_dock_status()
		self.undock_ac.wait_for_server() # Wait till its ready
		undock_goal = Undock.Goal() # Make goal
		self.undock_ac.send_goal(undock_goal) # Send goal blocking
		
		time.sleep(1)
		self.chirp(end_note)


	def reset_pose(self):
		"""
		This function resets the robot's pose estimate.
		"""
		try:
			# Create a request object
			request = ResetPose.Request()

			# Call the service asynchronously
			response = self.reset_pose_srv.call_async(request)

			if response is not None:
				self.get_logger().info('ResetPose service called successfully.')
				time.sleep(1)
			else:
				self.get_logger().error('No response from ResetPose service.')

		except Exception as e:
			self.get_logger().error('Failed to call ResetPose service: %r' % (e,))



	def record_pose(self):
		"""
		Store the current pose for future use.
		"""

		self.dock_sensor.publish_odometry()
		time.sleep(1) # Provides enough time to 
		if self.latest_pose_stamped is not None:
			self.recorded_pose = self.latest_pose_stamped
			self.get_logger().info("Pose recorded.")
		else:
			self.get_logger().error("No current pose available to record.")



	def drive_amnt(self, distance):
		"""
		Drive a certain distance.
		"""
		print("driving")

		self.chirp(start_note)
		self.drive_ac.wait_for_server()
		drive_goal = DriveDistance.Goal()
		drive_goal.distance = distance
		self.drive_ac.send_goal(drive_goal)
		
		time.sleep(1)  # Consider using async
		self.chirp(end_note)



	def rotate_amnt(self, angle):
		"""
		Rotate by a certain angle.
		"""
		print("rotating")
		self.chirp(start_note)
		self.rotate_ac.wait_for_server()
		rotate_goal = RotateAngle.Goal()
		rotate_goal.angle = angle
		self.rotate_ac.send_goal(rotate_goal)
		
		time.sleep(1)  # Consider using async
		self.chirp(end_note)



	def navigate_to_recorded_pose(self):
		"""
		Navigate back to the stored pose.
		"""
		self.chirp(start_note)
		print("Navigating back to home position from Odometry reading (PoseStamped)")
		if self.recorded_pose is not None:
			goal_msg = NavigateToPosition.Goal()
			goal_msg.goal_pose = self.recorded_pose
			goal_msg.achieve_goal_heading = True
			goal_msg.max_translation_speed = 0.3
			goal_msg.max_rotation_speed = 1.9

			self.nav_to_pos_ac.wait_for_server()
			self.nav_to_pos_ac.send_goal(goal_msg)
			self.chirp(ready_notes)
		else:
			self.chirp(error_notes)
			self.get_logger().error("No pose has been recorded.")



	def initiate_docking_sequence(self, msg):
		print("Docking sequence initiated")
		# ir_sensor.ir_opcode_poll()
		# mock_msg = IrOpcode()
		# mock_msg.opcode = 164
		# mock_msg.dock_sensor = IrOpcode.SENSOR_OMNI
		# print(f"Using mock IR opcode: {mock_msg.opcode}")


		# self.ir_sensor.ir_opcode_callback(mock_msg)
		# ir_sensor.ir_opcode_callback()

		ir_sensor.ir_intensity_poll()

		########### ########### ############ ########### 
		# max_attempts = 10000
		# attempts = 0
		# while attempts < max_attempts:
		# 	attempts += 1
		# 	print("Attempt No.:", attempts)
		# 	dock_sensor.publish_dock_status()
		# 	cur_value = dock_sensor.current_dock_status
		# 	if cur_value == 'True':
		# 		print("Docking successful")
		# 		break
		# 	# Add your actions here
		# 	elif cur_value == 'False':
		# 		ir_sensor.ir_intensity_poll()
		# 	time.sleep(1)

		for attempt_count in range(1, 10001):
			print(f"Docking Attempt: {attempt_count}")
			dock_sensor.publish_dock_status()
			if dock_sensor.current_dock_status == 'True':
				print("Docking successful")
				break
			elif dock_sensor.current_dock_status == 'False':
				ir_sensor.ir_intensity_poll()
			time.sleep(1)



	def takeoff(self):
		"""
		Orchestrates a series of actions: undock and drive, rotate a random amount, and drive forward a certain distance.
		"""
		# try:
		# 	self.undock()
		# 	self.reset_pose()
		# 	self.record_pose()
		# 	self.drive_amnt(0.1)
		# 	random_angle = random.uniform(-pi, pi)  # Random angle between -pi and pi
		# 	self.rotate_amnt(random_angle)
		# 	self.drive_amnt(0.1)  # Drive forward half a meter
		# 	self.navigate_to_recorded_pose()
		# 	self.rotate_amnt(pi)
		# 	# self.initiate_docking_sequence(self)
		# except Exception as error:
		# 	roomba.chirp(error_notes)
		# 	self.get_logger().error(f"Error in takeoff: {error}") # Error logging

		self.initiate_docking_sequence(self) ######## Now working on auto-docking sequence


if __name__ == '__main__':
	# rclpy.init()

	roomba = Roomba(namespace)
	exec = MultiThreadedExecutor(8)
	exec.add_node(roomba)
	exec.add_node(dock_sensor)
	exec.add_node(ir_sensor)

	# roomba.chirp(ready_notes)


	keycom = KeyCommander([
		(KeyCode(char='u'), roomba.takeoff),
	])
	print(" Press 'U' to intitiate launch")

	try:
		exec.spin()  # execute Roomba callbacks until shutdown or destroy is called
	except KeyboardInterrupt:
		print("KeyboardInterrupt, shutting down.")
	except Exception as error:
		print(f"Unexpected error: {error}")
	finally:
		exec.shutdown()
		roomba.destroy_node()
		rclpy.try_shutdown()

