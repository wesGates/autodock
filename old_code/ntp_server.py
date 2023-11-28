# navigate_to_position_server.py
# // Roomba_skeleton
import rclpy
from rclpy.node import Node
from rclpy.action.client import ActionClient
from rclpy.action import ActionServer
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup

# Create3 packages
from irobot_create_msgs.action import DriveDistance, Undock, RotateAngle, AudioNoteSequence, NavigateToPosition
from irobot_create_msgs.msg import AudioNote, AudioNoteVector
from builtin_interfaces.msg import Duration
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Quaternion

# Python packages
import random
import numpy as np

class NavigateToPositionServer(Node):

    def __init__(self):
        super().__init__('navigate_to_position_server')
        self.action_server = ActionServer(
            self,
            NavigateToPosition,
            'navigate_to_position',
            self.execute_callback)

    def execute_callback(self, goal_handle):
        # Implementation of how the goal is processed
        feedback_msg = NavigateToPosition.Feedback()
        # ... handle the action goal ...
        goal_handle.succeed()

        result = NavigateToPosition.Result()
        # ... set the action result ...
        return result

def main(args=None):
    rclpy.init(args=args)
    node = NavigateToPositionServer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
