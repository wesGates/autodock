import rclpy
from rclpy.node import Node
from irobot_create_msgs.msg import IrOpcode
from std_msgs.msg import String, Int8, UInt8
import irobot_create_msgs
from rclpy.qos import qos_profile_sensor_data

class IrOpcodePublisher(Node):
    def __init__(self, namespace):
        super().__init__('ir_opcode_publisher')
        
        # This is what 'sends' the data to the 'main' node
        self.publisher_ = self.create_publisher(IrOpcode, 'ir_opcode', 10) #return type, topic name, queue size
        # This subscribes to the /dock_status topic
        self.subscriber_ = self.create_subscription(IrOpcode, f'/{namespace}/ir_opcode', 
            self.listener, qos_profile_sensor_data)
        # This will hold the current value from the topic
        self.curValue = 0 # Blank inital string
        
        
    def listener(self, msg):
        """
        This will be called everytime the subscriber recieves a new message from the topic
        """
        if msg.opcode != 161:
            self.curValue = msg.opcode
    	
    def poll(self):
        """
        This will be called by the 'main' node to prevent overloading it with messages
        """
        msg = IrOpcode()
        msg.opcode = self.curValue
        self.publisher_.publish(msg)
