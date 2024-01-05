# ROS packages
import rclpy
from rclpy.node import Node
from rclpy.action.client import ActionClient
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup
from builtin_interfaces.msg import Duration
# Create3 packages
import irobot_create_msgs
from irobot_create_msgs.action import DriveDistance, Undock, RotateAngle, AudioNoteSequence
# Your ROS Node packages
from check_sensor import DockStatusPublisher
from check_iropcode import IrOpcodePublisher
# Garrett packages (Easy program start)
from pynput.keyboard import KeyCode
from key_commander import KeyCommander
# Python packages
from std_msgs.msg import String
from irobot_create_msgs.msg import AudioNote, AudioNoteVector, IrOpcode, IrIntensity

import random
import time

# Globals

rclpy.init()

start_note_duration = Duration(sec=0, nanosec=40000000)
end_note_duration = Duration(sec=0, nanosec=40000000)

start_note = [AudioNote(frequency=600, max_runtime=start_note_duration)]
end_note = [AudioNote(frequency=784, max_runtime=end_note_duration)]

class Roomba(Node):
	def __init__(self, namespace):
		super().__init__("robot")
		
		cb_Subscriptions0 = MutuallyExclusiveCallbackGroup()
		cb_Subscriptions1 = MutuallyExclusiveCallbackGroup()
		cb_Subscriptions2 = MutuallyExclusiveCallbackGroup()
		cb_Subscriptions3 = MutuallyExclusiveCallbackGroup()
		
		# Callback Groups
		#cb_Subscripions = MutuallyExclusiveCallbackGroup()
		cb_Actions = MutuallyExclusiveCallbackGroup()
		
		# Subscriptions
		self.subscription = self.create_subscription(String,'/check_dock_status',
			self.listener_callback, 10, callback_group=cb_Subscriptions0)
			
		self.ir_opcode_subscription = self.create_subscription(IrOpcode,'/ir_opcode',  
			self.ir_opcode_callback, 10, callback_group=cb_Subscriptions1)
			
		self.ir_intensity_subscription = self.create_subscription(IrIntensity,'/check_ir_intensity',
			self.ir_intensity_callback,10, callback_group=cb_Subscriptions2)

		self.latest_ir_intensity = 0
		self.docking_ir_threshold = 100
		
		# Actions
		self.undock_ac = ActionClient(self, Undock, f'/{namespace}/undock',
			callback_group=cb_Actions)
		self.drive_ac = ActionClient(self, DriveDistance, f'/{namespace}/drive_distance',
			callback_group=cb_Actions)
		self.rotate_ac = ActionClient(self, RotateAngle, f'/{namespace}/rotate_angle',
			callback_group=cb_Actions)
		self.audio_ac = ActionClient(self, AudioNoteSequence, f'/{namespace}/audio_note_sequence',
		 	callback_group=cb_Actions)
		 	
		self.last_rotation = 0.0
	
	def listener_callback(self,msg):
		"""
		This function will run when the subscription receives a message from the publisher
		"""
		print("I got: ",msg.data)
		
	def ir_intensity_callback(self, msg):
		"""
		Callback for IR intensity readings
		"""
		self.latest_ir_intensity = msg.data
		self.get_logger().info(f'IR Intensity: {self.latest_ir_intensity}')
		
	def drive(self):
		sensor.poll()
		irOpcode.poll()
		# # Undock
		# self.undock_ac.wait_for_server()
		# undock_goal = Undock.Goal()
		# self.undock_ac.send_goal(undock_goal)
		# time.sleep(1)
		# self.play_chirp(start_note)
		
		# # Drive
		# self.drive_ac.wait_for_server()
		# drive_goal = DriveDistance.Goal()
		# drive_goal.distance = 0.2 # 1 meter
		# self.drive_ac.send_goal(drive_goal)
		# time.sleep(1)
		# self.play_chirp(start_note)
		
		# # Turn
		# self.rotate_ac.wait_for_server()
		# rotate_goal = RotateAngle.Goal()
		# rotate_goal.angle = random.uniform(-3.13, 3.14)
		# self.last_rotation = rotate_goal.angle
		# self.rotate_ac.send_goal(rotate_goal)
		# time.sleep(1)
		# self.play_chirp(start_note)
		
		# # Drive
		# drive_goal.distance = 0.2
		# self.drive_ac.send_goal(drive_goal)
		# time.sleep(1)
		# self.play_chirp(start_note)
		
		# # Dock
		# self.rotate_ac.wait_for_server()	
		# reverse_rotate_goal = RotateAngle.Goal()
		# reverse_rotate_goal.angle = 3.1
		# self.rotate_ac.send_goal(reverse_rotate_goal)
		# time.sleep(1)
		# self.play_chirp(start_note)
		# self.reverse_path()
			
		# time.sleep(1)
		# self.play_chirp(start_note)
		
		sensor.poll()
		for _ in range(50):
			if sensor.poll() == 'True':
				break
			time.sleep(2)
			irOpcode.poll()
			time.sleep(2)
			
		sensor.poll()
		
		
	def reverse_path(self):

		self.drive_ac.wait_for_server()
		reverse_drive_goal = DriveDistance.Goal()
		reverse_drive_goal.distance = 0.5
		self.drive_ac.send_goal(reverse_drive_goal)
		time.sleep(1)
		self.play_chirp(start_note)
		
		self.rotate_ac.wait_for_server()
		reverse_rotate_goal = RotateAngle.Goal()
		reverse_rotate_goal.angle = -self.last_rotation
		self.rotate_ac.send_goal(reverse_rotate_goal)
		time.sleep(1)
		self.play_chirp(start_note)
		
		reverse_drive_goal.distance = 0.2
		self.drive_ac.send_goal(reverse_drive_goal)
		time.sleep(1)
		self.play_chirp(start_note)
		self.docking_ir_threshold = 0
		
	def play_chirp(self,send_notes):
	
		self.audio_ac.wait_for_server()
		
		audio_goal = AudioNoteSequence.Goal()
		audio_goal.iterations = 1
		audio_goal.note_sequence = AudioNoteVector(notes=send_notes)
		self.audio_ac.send_goal_async(audio_goal)
		
	def ir_opcode_callback(self, msg):
		"""
		Handle the IR opcode messages
		"""	    
		"""
		Start docking process if IR intensity is above a certain threshold
		"""
		print(msg.opcode)
		if self.latest_ir_intensity >= self.docking_ir_threshold:
			if msg.opcode == 0:
				self.get_logger().info('IR intensity too low for docking')   
			elif msg.opcode == 164:
				self.adjust_position(turn_right=True, move_forward=False)
			elif msg.opcode == 165:
					# Too far left and close, move back and turn right
					self.adjust_position(turn_right=True, move_forward=False, move_back=True)
			elif msg.opcode == 168:
					# Too far on the right, turn left
					self.adjust_position(turn_left=True, move_forward=False)
			elif msg.opcode == 169:
					# Too far right and close, move back and turn left
					self.adjust_position(turn_left=True, move_forward=False, move_back=True)
			elif msg.opcode == 172:
					# Heading in the right direction, move forward
					self.adjust_position(move_forward=True)
			elif msg.opcode == 173:
					# Docked
					self.docking_ir_threshold = 1000000
					rclpy.shutdown()
					print("Docked successfully")


	def adjust_position(self, turn_right=False, move_forward=False, move_back=False, turn_left=False):
			"""
			Adjust the robot's position based on IR sensor data
			"""
			if move_back:
				self.execute_drive(-0.03)
		
			if turn_right:
				self.execute_rotate(-0.1)
				
			if turn_left:
				self.execute_rotate(0.1)
		
			if move_forward:
				self.execute_drive(0.03)

	def execute_drive(self, distance):
			"""
			Drive a certain distance
			"""
			self.drive_ac.wait_for_server()
			drive_goal = DriveDistance.Goal()
			drive_goal.distance = distance
			self.drive_ac.send_goal(drive_goal)
			time.sleep(1)

	def execute_rotate(self, angle):
			"""
			Rotate by a certain angle
			"""
			self.rotate_ac.wait_for_server()
			rotate_goal = RotateAngle.Goal()
			rotate_goal.angle = angle
			self.rotate_ac.send_goal(rotate_goal)
			time.sleep(1)


if __name__ == '__main__':
		#rclpy.init()
	namespace = 'create3_0561'
	roomba = Roomba(namespace)
	irOpcode = IrOpcodePublisher(namespace)
	sensor = DockStatusPublisher(namespace)
	
	exec = MultiThreadedExecutor(5)
	exec.add_node(roomba)
	exec.add_node(irOpcode)
	exec.add_node(sensor)
		
	keycom = KeyCommander([
		(KeyCode(char='s'), roomba.drive),
		])
	print("S")

	# Try/Except to shutdown "gracefully"
	try:
		exec.spin()
	except KeyboardInterrupt:
		rclpy.shutdown()
	finally:
		roomba.destroy_node()
		irOpcode.destroy_node()
		rclpy.shutdown()
