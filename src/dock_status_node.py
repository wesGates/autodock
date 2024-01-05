import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from std_msgs.msg import String
from irobot_create_msgs.msg import DockStatus
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry
from std_msgs.msg import Header, String, Int32, Float32, UInt8, Int16 # Some topics have specific datatypes (POTENTIALLY USELESS!!!)


class DockStatusMonitorNode(Node):
    def __init__(self, namespace):
        super().__init__('dock_sensor')

        # Publisher for DockStatus as a String
        self.dock_status_publisher_ = self.create_publisher(String, f'/{namespace}/check_dock_status', 10)

        # # Publisher for PoseStamped messages
        # self.pose_publisher_ = self.create_publisher(PoseStamped, f'/{namespace}/pose_stamped', 10)

        # Subscription to the dock_status topic to receive DockStatus messages
        self.dock_status_subscriber_ = self.create_subscription(DockStatus,f'/{namespace}/dock_status', 
                                                                self.dock_status_callback, qos_profile_sensor_data)

        # # Subscription to the odometry topic to receive Odometry messages
        # self.odometry_subscriber_ = self.create_subscription(Odometry, f'/{namespace}/odom', 
        #                                                         self.odometry_callback, qos_profile_sensor_data)

        # Variable initialization
        self.current_dock_status = None
        self.current_odometry = None



    def dock_status_callback(self, msg):
        # Update the dock status
        self.current_dock_status = msg.is_docked
        # self.current_dock_status = str(msg.is_docked) # Uncomment if you have troubles


    def publish_dock_status(self):
        # Create a String message with the current dock status
        msg = String()
        msg.data = str(self.current_dock_status)
        # Publish the message
        self.dock_status_publisher_.publish(msg)



    # def odometry_callback(self, odometry_msg):
    #     # Update the current odometry
    #     self.current_odometry = odometry_msg

    # def publish_odometry(self):
    #     # Check if we have received odometry data
    #     if self.current_odometry is not None:
    #         pose_stamped_msg = PoseStamped()
    #         pose_stamped_msg.header = self.current_odometry.header
    #         pose_stamped_msg.pose = self.current_odometry.pose.pose
    #         # print("published odometry (pose_stamped):", pose_stamped_msg)

    #         # Publish the PoseStamped message
    #         self.pose_publisher.publish(pose_stamped_msg)
    #         self.get_logger().info('PoseStamped message published.')




























# import rclpy
# from rclpy.node import Node
# from rclpy.qos import qos_profile_sensor_data
# from std_msgs.msg import String
# from irobot_create_msgs.msg import DockStatus

# class DockStatusMonitorNode(Node):
#     """
#     A ROS2 node to monitor and publish the docking status of an iRobot Create3.

#     This node subscribes to the /dock_status topic to receive real-time updates
#     on the robot's docking status and publishes this information to the
#     check_dock_status topic for use by other nodes.
#     """

#     def __init__(self, namespace):
#         """
#         Initialize the DockStatusMonitorNode.

#         Args:
#             namespace (str): The namespace of the robot, used to subscribe to the correct topics.

#         The constructor initializes the node, sets up a publisher to send data to other nodes,
#         and a subscriber to listen to the robot's docking status.
#         """
#         # Initialize the Node with the name 'dock_status_publisher'
#         super().__init__('dock_status_publisher')

#         # Publisher to send data to other nodes
#         # String is the message type for the published topic
#         self.dock_status_publisher_ = self.create_publisher(String, 'check_dock_status', 10)

#         # Subscriber to listen to the robot's dock status
#         # DockStatus is the expected message type from the /dock_status topic. Need to find that out from the docs.
#         self.dock_status_subscriber_ = self.create_subscription(DockStatus, f'/{namespace}/dock_status',
#                                                     self.dock_status_callback, qos_profile_sensor_data)

#         # Variable to hold the current value from the /dock_status topic
#         self.curValue = ''  # Initially an empty string

#     def dock_status_callback(self, msg): # was listener():
#         """
#         Callback for the /dock_status subscription.

#         Args:
#             msg (DockStatus): The message received from the /dock_status topic.

#         Updates the curValue attribute with the current docking status of the robot.
#         """
#         self.curValue = str(msg.is_docked)

#     def publish_dock_status(self): # was poll():
#         """
#         Publishes the current dock status.

#         This method is designed to control the publishing rate to avoid flooding
#         the network with messages. It should be called by the 'main' node when needed.
#         """
#         # Create a new String message
#         msg = String()
#         # Assign the current dock status to the message
#         msg.data = self.curValue
#         # Publish the message on the check_dock_status topic
#         self.dock_status_publisher_.publish(msg)


# # Example usage
# """"

# if __name__ == '__main__':
#     rclpy.init()
#     namespace = 'your_namespace_here'
#     dock_status_node = Dock_Status_Node(namespace)
#     rclpy.spin(dock_status_node)
#     dock_status_node.destroy_node()
#     rclpy.shutdown()

# """




















