# // Roomba_skeleton
import rclpy
from rclpy.node import Node
from rclpy.action.client import ActionClient
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup

# Create3 packages
from irobot_create_msgs.action import DriveDistance, Undock, RotateAngle, AudioNoteSequence, NavigateToPosition
from irobot_create_msgs.msg import AudioNote, AudioNoteVector
from builtin_interfaces.msg import Duration
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped

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

		# Actions
		self.undock_ac = ActionClient(self, Undock, f'/{namespace}/undock',
									  callback_group=cb_Actions)
		self.drive_ac = ActionClient(self, DriveDistance, f'/{namespace}/drive_distance',
									 callback_group=cb_Actions)
		self.audio_ac = ActionClient(self, AudioNoteSequence, f'/{namespace}/audio_note_sequence',
									 callback_group=cb_Actions)
		self.rotate_ac = ActionClient(self, RotateAngle, f'/{namespace}/rotate_angle', 
									callback_group=cb_Actions)
		self.navigate_to_position_ac = ActionClient(self, NavigateToPosition, f'/{namespace}/navigate_to_position')


	def listener_callback(self,msg):
		"""
		This function will run when the subscription receives a message from the publisher
		"""
		print("Callback msg: ",msg.data)

	def navigate_to_position(self, pose_stamped, achieve_goal_heading, max_translation_speed, max_rotation_speed):
		self.navigate_to_position_ac.wait_for_server()
		goal = NavigateToPosition.Goal()
		goal.goal_pose = pose_stamped
		goal.achieve_goal_heading = achieve_goal_heading
		goal.max_translation_speed = max_translation_speed
		goal.max_rotation_speed = max_rotation_speed

		# Send the goal and wait for the result (optional)
		self.navigate_to_position_ac.send_goal(goal)
		# self.navigate_to_position_ac.wait_for_result()



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

	def drive_forward(self):
		"""
		This function drives forward the prescribed distance
		"""
		self.chirp(start_note)

		self.drive_ac.wait_for_server()
		drive_goal = DriveDistance.Goal()
		drive_goal.distance = 0.2
		self.drive_ac.send_goal(drive_goal)

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
		self.chirp(start_note)

		random_angle = random.uniform(-pi, pi)
		print("Rotating randomly by angle:", random_angle)

		# Store the random r0tation angle for future use
		self.last_rotation_angle = random_angle

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

		rotate_angle = pi
		self.rotate_ac.wait_for_server()



		# Create and send the goal
		rotate_goal = RotateAngle.Goal()
		rotate_goal.angle = rotate_angle 
		self.rotate_ac.send_goal(rotate_goal)



	def rotate_troubleshooting(self):
		"""
		Moves a defined angle
		"""
		self.chirp(end_note)

		rotate_angle = pi/2
		self.rotate_ac.wait_for_server()
		print("Rotated predetermined amount:", rotate_angle)



		# Create and send the goal
		rotate_goal = RotateAngle.Goal()
		rotate_goal.angle = rotate_angle 
		self.rotate_ac.send_goal(rotate_goal)
		self.chirp(end_note)
		


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

		# Create and send the goal
		rotate_goal = RotateAngle.Goal()
		rotate_goal.angle = undo_angle
		self.rotate_ac.send_goal(rotate_goal)




