# // Roomba_skeleton
import rclpy
from rclpy.node import Node
from rclpy.action.client import ActionClient
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup

# Create3 packages
from irobot_create_msgs.action import DriveDistance, Undock, RotateAngle, AudioNoteSequence
from irobot_create_msgs.msg import AudioNote, AudioNoteVector
from builtin_interfaces.msg import Duration
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from irobot_create_msgs.srv import ResetPose
# import tf_transformations  # This library helps with transforming ROS data types


# Python packages
import random


# Globals
start_note = [ AudioNote(frequency=600, max_runtime=Duration(sec=0, nanosec= 50000000))]
end_note =   [ AudioNote(frequency=784, max_runtime=Duration(sec=0, nanosec= 50000000))]
pi = 3.141592654

class Roomba(Node):
	def __init__(self, namespace, sensor): # Must be passed a sensor parameter
		super().__init__("robot")
		self.sensor = sensor

		self.last_rotation_angle = None ##### Used for docking (NOTE: START )
		self.cumulative_rotation_angle = pi
		
		# Callback Groups
		cb_Subscriptions = MutuallyExclusiveCallbackGroup()
		cb_Actions = MutuallyExclusiveCallbackGroup()
		
		# Subscriptions
		self.subscription = self.create_subscription(String, '/check_dock_status',
													 self.listener_callback, 10, callback_group=cb_Subscriptions)
		# self.odom_subscription = self.create_subscription(Odometry, '/odom', 
		# 											self.odom_callback, 10, callback_group=cb_Subscriptions)

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
		self.undock_ac.send_goal(undock_goal) # Send goal blocking

		# Drive out 1 meter from being undocked
		self.chirp(start_note)
		self.drive_ac.wait_for_server()
		drive_goal = DriveDistance.Goal()
		drive_goal.distance = 0.3 # 1 meter
		self.drive_ac.send_goal(drive_goal)

		# Read current dock status
		self.sensor.poll()

	def drive_forward(self):
		"""
		This function drives forward the prescribed distance
		"""
		self.chirp(start_note)
		self.reset_pose()

		self.drive_ac.wait_for_server()
		drive_goal = DriveDistance.Goal()
		drive_goal.distance = 0.2
		self.drive_ac.send_goal(drive_goal)

	def chirp(self, sent_notes):
		"""
		This function plays a given chirp sequence.
		"""
		self.audio_ac.wait_for_server()
		self.reset_pose()

		goal = AudioNoteSequence.Goal()
		goal.iterations = 1
		goal.note_sequence = AudioNoteVector(notes=sent_notes)  # Wrap the notes in an AudioNoteVector

		# Send the goal
		self.audio_ac.send_goal_async(goal)

	def rotate_randomly(self):
		"""
		Generates a random angle between pi and -pi, then rotates and returns the rotation_angle value
		"""
		self.chirp(start_note)
		self.reset_pose()

		random_angle = random.uniform(-pi, pi)
		print("Rotating randomly by angle:", random_angle)

		# Store the random r0tation angle for future use
		self.last_rotation_angle = random_angle

		# # Update the cumulative rotation angle
		# self.cumulative_rotation_angle += random_angle
		# print("Updated cumulative rotation angle:", self.cumulative_rotation_angle)
		# rotate_goal = self.cumulative_rotation_angle

		self.rotate_ac.wait_for_server()
		
		# Create and send the goal
		rotate_goal = RotateAngle.Goal()
		rotate_goal.angle = random_angle 
		self.rotate_ac.send_goal(rotate_goal)


	def rotate_180(self):
		"""
		Turns around
		"""
		self.chirp(start_note)
		self.reset_pose()

		rotate_angle = pi
		self.rotate_ac.wait_for_server()

		# # Update the cumulative rotation angle
		# self.cumulative_rotation_angle += rotate_angle
		# print("Updated cumulative rotation angle:", self.cumulative_rotation_angle)
		# rotate_goal = self.cumulative_rotation_angle

		# Create and send the goal
		rotate_goal = RotateAngle.Goal()
		rotate_goal.angle = rotate_angle 
		self.rotate_ac.send_goal(rotate_goal)


	def rotate_troubleshooting(self):
		"""
		Moves a defined angle
		"""
		self.chirp(end_note)
		self.reset_pose()

		rotate_angle = pi/4
		self.rotate_ac.wait_for_server()
		print("Rotated predetermined amount:", rotate_angle)

		# # Update the cumulative rotation angle
		# self.cumulative_rotation_angle += rotate_angle
		# print("Updated cumulative rotation angle:", self.cumulative_rotation_angle)
		# rotate_goal = self.cumulative_rotation_angle

		# Create and send the goal
		rotate_goal = RotateAngle.Goal()
		rotate_goal.angle = rotate_angle 
		self.rotate_ac.send_goal(rotate_goal)
		

	def undo_random_rotation(self):
		"""
		Rotates the robot by the negative of the last rotation angle to undo the rotation
		"""
		if self.last_rotation_angle is None:
			print("No previous rotation to undo")
			return
		self.reset_pose()

		undo_angle = -self.last_rotation_angle
		print("Undoing rotation by angle:", undo_angle)

		self.rotate_ac.wait_for_server()

		# # Update the cumulative rotation angle
		# self.cumulative_rotation_angle += undo_angle
		# print("Updated cumulative rotation angle:", self.cumulative_rotation_angle)
		# rotate_goal = self.cumulative_rotation_angle

		# Create and send the goal
		rotate_goal = RotateAngle.Goal()
		rotate_goal.angle = undo_angle
		self.rotate_ac.send_goal(rotate_goal)

	def reset_pose(self):
		"""
		This function resets the robot's pose estimate.
		"""
		try:
			# Create a request object
			request = ResetPose.Request()
			# Modify the request as needed, e.g., set a new pose

			# Call the service
			future = self.reset_pose_service.call_async(request)
			rclpy.spin_until_future_complete(self, future)
			response = future.result()
			# Handle the response as needed
		except Exception as e:
			self.get_logger().error('Failed to call ResetPose service: %r' % (e,))




