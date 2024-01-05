# // Roomba_skeleton
# ROS Imports
import rclpy
from rclpy.node import Node
from rclpy.action.client import ActionClient
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup
from rclpy.executors import SingleThreadedExecutor
from rclpy.executors import MultiThreadedExecutor
from rclpy.qos import qos_profile_sensor_data
from numpy import uint8


# Create3 Packages
from irobot_create_msgs.action import DriveDistance, Undock, RotateAngle, AudioNoteSequence
from irobot_create_msgs.msg import AudioNote, AudioNoteVector
from irobot_create_msgs.srv import ResetPose
from builtin_interfaces.msg import Duration
from irobot_create_msgs.msg import  IrOpcode

# Python Packages

from math import pi
from threading import RLock
from std_msgs.msg import Float32, UInt8, _u_int8, Int8, String # Some topics have specific datatypes

class IrMonitorNode(Node):
	def __init__(self, namespace):
		super().__init__('ir_sensor')
		
		# Publishers
		self.opcode_publisher_ = self.create_publisher(String, 'ir_opcode_number', 10)

		# Subscriptions
		self.opcode_subscriber = self.create_subscription(IrOpcode, f'/{namespace}/ir_opcode', 
														  self.ir_opcode_listener, qos_profile_sensor_data)
		
		# Variable Initialization for storing published information
		self.current_opcode = None


	def ir_opcode_listener(self, msg):
		""" 
		Constantly updates the opcode message from the /ir_opcode topic.
		This includes a bunch of info that will be filtered out in the publisher.
		"""
		self.current_opcode = msg.opcode # Containes all the opcode information (a lot of stuff we dont need.



	def publish_ir_opcode(self):
		""" This method publishes the opcode value as a UInt8 message to all subscribers """
		msg = String()
		msg.data = str(self.current_opcode)

		self.opcode_publisher_.publish(msg)
		return self.current_opcode



		 
