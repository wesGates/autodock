# // Roomba_skeleton
# ROS Imports
import rclpy
from rclpy.node import Node
from rclpy.action.client import ActionClient
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup
from rclpy.executors import SingleThreadedExecutor
from rclpy.executors import MultiThreadedExecutor
from rclpy.qos import qos_profile_sensor_data


# Create3 Packages
from irobot_create_msgs.action import DriveDistance, Undock, RotateAngle, AudioNoteSequence
from irobot_create_msgs.msg import AudioNote, AudioNoteVector
from irobot_create_msgs.srv import ResetPose
from builtin_interfaces.msg import Duration
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from irobot_create_msgs.msg import IrIntensityVector, IrOpcode

# Python Packages
import random
import time
from math import pi
from threading import RLock
from std_msgs.msg import Float32, UInt8, Int8 # Some topics have specific datatypes

# Rlock = RLock()

class IrMonitorNode(Node):
	def __init__(self, namespace):
		super().__init__('ir_publisher')
		
		# Publishers
		self.opcode_publisher = self.create_publisher(UInt8, 'ir_opcode', 10)
		self.intensity_publisher = self.create_publisher(Int8, 'ir_intensity', 10)

		# Subscriptions
		self.opcode_subscriber = self.create_subscription(IrOpcode, f'/{namespace}/ir_opcode', 
															 self.ir_opcode_callback, qos_profile_sensor_data)
		self.intensity_subscriber = self.create_subscription(IrIntensityVector, f'/{namespace}/ir_intensity', 
															 self.ir_intensity_callback, qos_profile_sensor_data)


		# Variable Initialization
		self.curOpcode = None
		self.curIr_Intensity = None


	def ir_intensity_callback(self, ir_intensity_msg): 		########### ########### ############ ########### CHANGE THIS, OLD CODE

		"""
		This will be called everytime the subscriber receives a new message from the topic
		"""
		self.curIr_Intensity = ir_intensity_msg.readings
		for i in self.curIr_Intensity:
			return(f"IR Intensity: {i.header.frame_id}, {i.value}") # This directly returns the value. Better to publish? 


	def ir_opcode_callback(self, msg): ########### ########### ############ ########### CHANGE THIS, OLD CODE
		opcode_actions = {
			164: {'turn_right': True, 'move_forward': False},
			165: {'turn_right': True, 'move_forward': False, 'move_back': True},
			168: {'turn_right': False, 'move_forward': False},
			169: {'turn_right': False, 'move_forward': False, 'move_back': True},
			172: {'move_forward': True},
			173: {'docked': True}
		}

		action = opcode_actions.get(msg.opcode, {})
		print(f"Action determined from opcode: {action}")

		if 'docked' in action:
			print("Docked")
		else:
			self.drive_adjust(**action)
			print(f"Adjusting position: {'Turning right' if action.get('turn_right', False) else 'Not turning right'}, {'Moving forward' if action.get('move_forward', False) else 'Not moving forward'}, {'Moving back' if action.get('move_back', False) else ''}".strip())


	# def dock_status_callback(self, isdocked_msg):
	# 	"""
	# 	This will be called everytime the subscriber receives a new message from the topic
	# 	"""
	# 	self.curValue_1 = isdocked_msg.sensor
	# 	self.poll_called = False
	# 	# print(self.curValue_1)


	def drive_adjust(self, turn_right=False, move_forward=False, move_back=False):		########### ########### ############ ########### CHANGE THIS, OLD CODE

		"""
		Modify the robot's position based on IR sensor data. The arguments are false by default,
		and altered via process_ir_opcode.

		Distances are in meters
		Rotations are in radians
		"""
		if move_back:
			self.sendDriveGoal(-0.05)

		if turn_right:
			self.sendRotateGoal(-pi/16)

		elif not turn_right:
			self.sendRotateGoal(pi/16)

		if move_forward:
			self.sendDriveGoal(0.05)

	# def ir_opcode_poll(self):
	# 	if self.curValue_1 is not None and not self.poll_called:
	# 		print("Sensor Data: ", self.curValue_1)

	# 		self.poll_called = True

	def ir_intensity_poll(self): 		########### ########### ############ ########### CHANGE THIS, OLD CODE

		if self.curIr_Intensity is not None and len(self.curIr_Intensity) > 0:
			# Iterate over all readings in curValue_2
			for index, reading in enumerate(self.curIr_Intensity):
				print(f"{reading.header.frame_id}  {reading.value}")

         
