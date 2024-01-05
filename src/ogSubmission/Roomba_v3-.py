# // Roomba_skeleton
import rclpy
from rclpy.node import Node
from rclpy.action.client import ActionClient
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup

# Create3 packages
from irobot_create_msgs.action import DriveDistance, Undock, RotateAngle, AudioNoteSequence, IrOpcode
from irobot_create_msgs.msg import AudioNote, AudioNoteVector
from builtin_interfaces.msg import Duration
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from irobot_create_msgs.srv import ResetPose
# import tf_transformations  # This library helps with transforming ROS data types

from rclpy.executors import SingleThreadedExecutor

# Python packages
import random
import time


# Globals
start_note = [ AudioNote(frequency=600, max_runtime=Duration(sec=0, nanosec= 50000000))]
end_note =   [ AudioNote(frequency=784, max_runtime=Duration(sec=0, nanosec= 50000000))]
rand_note =  [ AudioNote(frequency=350, max_runtime=Duration(sec=0, nanosec= 150000000))]
pi = 3.141592654

# Vars to change for class
distance_1 = 0.3
distance_2 = 0.2

class Roomba(Node):
	def __init__(self, namespace, sensor): # Must be passed a sensor parameter
		super().__init__("robot")
		self.sensor = sensor

		# Callback Groups
		cb_Subscriptions = MutuallyExclusiveCallbackGroup()
		cb_Actions = MutuallyExclusiveCallbackGroup()
		
		# Subscriptions
		self.subscription = self.create_subscription(String, '/check_dock_status',
													 self.listener_callback, 10, callback_group=cb_Subscriptions)
		self.subscription = self.create_subscription(IrOpcode,'/check_iropcode',  
													self.ir_opcode_callback, 10, callback_group= cb_Subscriptions)

		# Actions
		self.undock_ac = ActionClient(self, Undock, f'/{namespace}/undock',
									  callback_group=cb_Actions)
		self.drive_ac = ActionClient(self, DriveDistance, f'/{namespace}/drive_distance',
									 callback_group=cb_Actions)
		self.audio_ac = ActionClient(self, AudioNoteSequence, f'/{namespace}/audio_note_sequence',
									 callback_group=cb_Actions)
		self.rotate_ac = ActionClient(self, RotateAngle, f'/{namespace}/rotate_angle', 
									callback_group=cb_Actions)
		
		# ResetPose service client
		self.reset_pose_service = self.create_client(ResetPose, f'/{namespace}/reset_pose')

		# Ensure service is available
		while not self.reset_pose_service.wait_for_service(timeout_sec=1.0):
			self.get_logger().info('ResetPose service not available, waiting again...')

	def listener_callback(self,msg):
		"""
		This function will run when the subscription receives a message from the publisher
		"""
		print("Callback msg: ",msg.data)


	def undock_and_drive(self):
		"""
		This function undocks and drives out a given distance
		"""
		self.chirp(start_note)
		self.reset_pose()

		# Read current dock status
		self.sensor.poll()  # Now self.sensor is defined within the class scope

		# Undock
		self.chirp(start_note)
		self.undock_ac.wait_for_server() # Wait till its ready
		undock_goal = Undock.Goal() # Make goal
		self.undock_ac.send_goal_async(undock_goal) # Send goal blocking


		# Drive out 1 meter from being undocked
		self.chirp(start_note)

		self.drive_ac.wait_for_server()
		drive_goal = DriveDistance.Goal()
		drive_goal.distance = distance_1_meter # 1 meter
		self.drive_ac.send_goal_async(drive_goal)

		# Read current dock status
		self.sensor.poll()
		self.reset_pose()

	def drive_forward(self):
		"""
		This function drives forward the prescribed distance
		"""
		self.chirp(start_note)
		self.reset_pose()

		self.drive_ac.wait_for_server()
		drive_goal = DriveDistance.Goal()
		drive_goal.distance = distance_half_meter
		self.drive_ac.send_goal_async(drive_goal)

	def drive_amnt(self, distance): # Used for making small adjustments to robot position
			"""
			Drive a certain distance
			"""
			self.chirp(start_note)
			self.reset_pose()
			self.drive_ac.wait_for_server()
			drive_goal = DriveDistance.Goal()
			drive_goal.distance = distance
			self.drive_ac.send_goal(drive_goal)
			time.sleep(1) ##################################### Consider using async
			self.chirp(end_note)

	def rotate_amnt(self, angle): # Used for making small adjustments to robot heading
			"""
			Rotate by a certain angle
			"""
			self.chirp(start_note)
			self.reset_pose()
			self.rotate_ac.wait_for_server()
			rotate_goal = RotateAngle.Goal()
			rotate_goal.angle = angle
			self.rotate_ac.send_goal(rotate_goal)
			time.sleep(1) ####################################### Consider using async
			self.chirp(end_note)

	def chirp(self, sent_notes):
		"""
		This function plays a given chirp sequence.
		"""
		self.audio_ac.wait_for_server()

		goal = AudioNoteSequence.Goal()
		goal.iterations = 1
		goal.note_sequence = AudioNoteVector(notes=sent_notes)  # Wrap the notes in an AudioNoteVector

		# Send the goal
		self.audio_ac.send_goal_async(goal)

	def rotate_randomly(self):
		"""
		Generates a random angle between pi and -pi, then rotates and returns the rotation_angle value
		"""
		self.reset_pose()
		# time.sleep(5)
		self.chirp(rand_note)

		random_angle = random.uniform(-pi, pi)
		print("Rotating randomly by angle:", random_angle)

		# Store the random r0tation angle for future use
		self.last_rotation_angle = random_angle

		self.rotate_ac.wait_for_server()
		
		# Create and send the goal
		rotate_goal = RotateAngle.Goal()
		rotate_goal.angle = random_angle 
		self.rotate_ac.send_goal_async(rotate_goal)
		
		self.chirp(rand_note)



	def rotate_180(self):
		"""
		Turns around
		"""
		self.chirp(start_note)
		self.reset_pose()

		rotate_angle = pi
		self.rotate_ac.wait_for_server()

		print("Defined rotation:", rotate_angle)

		# Create and send the goal
		rotate_goal = RotateAngle.Goal()
		rotate_goal.angle = rotate_angle 
		self.rotate_ac.send_goal_async(rotate_goal)

		self.chirp(end_note)


	def rotate_troubleshooting(self):
		"""
		Moves a defined angle
		"""
		self.chirp(end_note)
		self.reset_pose()

		rotate_angle = pi/4
		self.rotate_ac.wait_for_server()

		# Store the random r0tation angle for future use
		self.last_rotation_angle = rotate_angle
		print("Rotated predetermined amount:", rotate_angle)

		# Create and send the goal
		rotate_goal = RotateAngle.Goal()
		rotate_goal.angle = rotate_angle 
		self.rotate_ac.send_goal_async(rotate_goal)
		

	def undo_random_rotation(self):
		"""
		Rotates the robot by the negative of the last rotation angle to undo the rotation
		"""
		self.chirp(end_note)

		if self.last_rotation_angle is None:
			print("No previous rotation to undo")
			return

		self.reset_pose()

		undo_angle = -self.last_rotation_angle
		print("Undoing rotation by angle:", undo_angle)

		self.rotate_ac.wait_for_server()

		# Create and send the goal
		rotate_goal = RotateAngle.Goal()
		rotate_goal.angle = undo_angle
		self.rotate_ac.send_goal_async(rotate_goal)
		
		self.chirp(start_note)

	def reset_pose(self):
		"""
		This function resets the robot's pose estimate. Useful when utilizing odometry navigation.
		"""
		try:
			# Create a request object
			request = ResetPose.Request()
			# Modify the request as needed, e.g., set a new pose

			# Call the service
			future = self.reset_pose_service.call_async(request)
			rclpy.spin_until_future_complete(self, future)
			response = future.result()
		except Exception as e:
			self.get_logger().error('Failed to call ResetPose service: %r' % (e,))

	def ir_opcode_callback(self, msg): ########## Revert to in case this is too much to debug
		opcode_actions = {
			164: {'turn_right': True, 'move_forward': False},
			165: {'turn_right': True, 'move_forward': False, 'move_back': True},
			168: {'turn_right': False, 'move_forward': False},
			169: {'turn_right': False, 'move_forward': False, 'move_back': True},
			172: {'move_forward': True},
			173: {'docked': True}
		}

		action = opcode_actions.get(msg.opcode, {})
		if 'docked' in action:
			print("Docked")
		else:
			self.drive_adjust(**action)
			print(f"Adjusting position: {'Turning right' if action.get('turn_right', False) else 'Not turning right'}, {'Moving forward' if action.get('move_forward', False) else 'Not moving forward'}, {'Moving back' if action.get('move_back', False) else ''}".strip())







