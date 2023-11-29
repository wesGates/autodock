# // Roomba_skeleton
import rclpy
from rclpy.node import Node
from rclpy.action.client import ActionClient
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup

# Create3 packages
from irobot_create_msgs.action import DriveDistance, Undock, RotateAngle, AudioNoteSequence, NavigateToPosition
from irobot_create_msgs.msg import AudioNote, AudioNoteVector, IrOpcode
from builtin_interfaces.msg import Duration
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Quaternion


# Python packages
import random
import numpy as np

# Globals
start_note = [ AudioNote(frequency=600, max_runtime=Duration(sec=0, nanosec= 50000000))]
end_note =   [ AudioNote(frequency=784, max_runtime=Duration(sec=0, nanosec= 50000000))]
navnode_note =   [ AudioNote(frequency=400, max_runtime=Duration(sec=0, nanosec= 50000000))]
pi = 3.141592654

class NavigatorNode(Node):
	def __init__(self, namespace, sensor): # Must be passed a sensor parameter
		super().__init__("robot")
		self.sensor = sensor

		# Callback Groups
		cb_Subscriptions = MutuallyExclusiveCallbackGroup()
		cb_Actions = MutuallyExclusiveCallbackGroup()

		# Subscriptions
		self.subscription = self.create_subscription(String, '/check_dock_status',
													 self.listener_callback, 10, callback_group=cb_Subscriptions)
		self.pose_subscription = self.create_subscription(PoseStamped, '/pose_topic', 
													self.pose_callback, 10, callback_group= cb_Subscriptions)
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
		self.navigate_to_position_ac = ActionClient(self, NavigateToPosition, f'/{namespace}/navigate_to_position',
											  callback_group=cb_Actions)
		
	def listener_callback(self,msg):
		"""
		This function will run when the subscription receives a message from the publisher
		"""
		print("Callback msg: ",msg.data)

	def pose_callback(self, msg):
		# Process the incoming pose data
		self.get_logger().info(f"Received pose: position {msg.pose.position}, orientation {msg.pose.orientation}")

	def send_navigation_goal(self, x, y, z, roll, pitch, yaw):
		self.chirp(navnode_note)
		pose_stamped = PoseStamped()
		print(pose_stamped)
		pose_stamped.header.frame_id = 'odom'
		pose_stamped.header.stamp = self.get_clock().now().to_msg()

		# Print the current values
		print("Position X:", pose_stamped.pose.position.x)
		print("Position Y:", pose_stamped.pose.position.y)
		print("Position Z:", pose_stamped.pose.position.z)
		print("Orientation X:", pose_stamped.pose.orientation.x)
		print("Orientation Y:", pose_stamped.pose.orientation.y)
		print("Orientation Z:", pose_stamped.pose.orientation.z)
		print("Orientation W:", pose_stamped.pose.orientation.w)


		quaternion = self.quaternion_from_euler(roll, pitch, yaw)
		print("Quaternion:", quaternion)
		pose_stamped.pose.orientation = Quaternion(
			x=quaternion[0], 
			y=quaternion[1], 
			z=quaternion[2],
			w=quaternion[3]
		)
		# print("DDDDDDDDDDDDDDDDDDD:", pose_stamped.pose)

		# # Set the current position and orientation values passed from the function call
		pose_stamped.pose.position.x = x
		pose_stamped.pose.position.y = y
		pose_stamped.pose.position.z = z
		pose_stamped.pose.orientation.x = quaternion[0]
		pose_stamped.pose.orientation.y = quaternion[1]
		pose_stamped.pose.orientation.z = quaternion[2]
		pose_stamped.pose.orientation.w = quaternion[3]

		print("MMMMMMMMMMMMMMM:", pose_stamped.pose)

		self.chirp(navnode_note)

		goal = NavigateToPosition.Goal()
		print("Goal:", goal)
		print("Stamped Pose:", pose_stamped)
		goal.goal_pose = pose_stamped
		goal.achieve_goal_heading = False
		# goal.achieve_goal_heading = True
		goal.max_translation_speed = 0.3
		goal.max_rotation_speed = 1.9

		self.navigate_to_position_ac.wait_for_server()
		print("Goal:", goal)
		self.navigate_to_position_ac.send_goal(goal)
		self.chirp(navnode_note)
		future = self.navigate_to_position_ac.send_goal_async(goal)
		future.add_done_callback(self.goal_response_callback)

	def goal_response_callback(self, future):
		goal_handle = future.result()
		if not goal_handle.accepted:
			self.get_logger().info('Goal rejected')
			return

		self.get_logger().info('Goal accepted')


	def quaternion_from_euler(self, roll, pitch, yaw):
		qx = np.sin(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) - np.cos(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
		qy = np.cos(roll/2) * np.sin(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.cos(pitch/2) * np.sin(yaw/2)
		qz = np.cos(roll/2) * np.cos(pitch/2) * np.sin(yaw/2) - np.sin(roll/2) * np.sin(pitch/2) * np.cos(yaw/2)
		qw = np.cos(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
		return [qx, qy, qz, qw]
	
	def undock_and_drive(self):
		"""
		This function undocks and drives out a given distance
		"""
		self.chirp(start_note)

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

		# # Print the latest odometry data after moving
		# self.print_latest_odometry()

	def drive_forward(self):
		"""
		This function drives forward the prescribed distance
		"""
		self.chirp(start_note)

		self.drive_ac.wait_for_server()
		drive_goal = DriveDistance.Goal()
		drive_goal.distance = 0.2
		self.drive_ac.send_goal(drive_goal)

		# # Print the latest odometry data after moving
		# self.print_latest_odometry()

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

		# self.audio_ac.wait_for_result()

	def rotate_randomly(self):
		"""
		Generates a random angle between pi and -pi, then rotates and returns the rotation_angle value
		"""
		self.chirp(start_note)

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

		# # Print the latest odometry data after moving
		# self.print_latest_odometry()

	def rotate_180(self):
		"""
		Turns around
		"""
		self.chirp(start_note)

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

		# # Print the latest odometry data after moving
		# self.print_latest_odometry()

	def rotate_troubleshooting(self):
		"""
		Moves a defined angle
		"""
		self.chirp(end_note)

		rotate_angle = 0.0
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
		
		# Print the latest odometry data after moving
		# self.print_latest_odometry()

	def undo_random_rotation(self):
		"""
		Rotates the robot by the negative of the last rotation angle to undo the rotation
		"""
		if self.last_rotation_angle is None:
			print("No previous rotation to undo")
			return

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

		# # Print the latest odometry data after moving
		# self.print_latest_odometry()# self.rotate_ac.wait_for_result()




