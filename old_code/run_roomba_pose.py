#// run_roomba
import rclpy
from rclpy.executors import MultiThreadedExecutor

# Garrett packages (Easy program start)
from pynput.keyboard import KeyCode
from key_commander import KeyCommander

# Import the Roomba class from myDock_audiostuff
from Roomba_skeleton_pose import NavigatorNode

# Your ROS Node packages 
from check_sensor import DockStatusPublisher

# Imports for AudioNote & Chirps
from std_msgs.msg import Header
from builtin_interfaces.msg import Duration
from irobot_create_msgs.msg import AudioNote, AudioNoteVector

import time

# Initialize the ROS client library, namespace, sensor, and class
rclpy.init()
namespace = 'create3_0561'
sensor = DockStatusPublisher(namespace)
navigator_node = NavigatorNode(namespace, sensor)

# Global
start_note = [ AudioNote(frequency=600, max_runtime=Duration(sec=0, nanosec= 50000000))]
end_note =   [ AudioNote(frequency=784, max_runtime=Duration(sec=0, nanosec= 50000000))]
pi = 3.141592654

# def main(x, y, z, roll, pitch, yaw):
  
#     # Sending a navigation goal
#     navigator_node.send_navigation_goal(x, y, z, roll, pitch, yaw)

if __name__ == '__main__':
    # rclpy.init()
    exec = MultiThreadedExecutor(3)
    exec.add_node(navigator_node)
    exec.add_node(sensor)

    navigator_node.send_navigation_goal(0.5, 0.5, 0.0, 0.0, 0.0, 0.5)

    # # KeyCommander Definitions
    # keycom1 = KeyCommander([
    #     (KeyCode(char='u'), navigator_node.undock_and_drive),
    # ])
    # print("Press 'U' to undock and move forward, or to move forward after being undocked")

    # keycom2 = KeyCommander([
    #     (KeyCode(char='r'), navigator_node.rotate_randomly),
    # ])
    # print("Press 'R' to rotate randomly")

    # keycom3 = KeyCommander([
    #     (KeyCode(char='f'), navigator_node.drive_forward),
    # ])
    # print("Press 'F' to move forward")

    # keycom4 = KeyCommander([
    #     (KeyCode(char='t'), navigator_node.rotate_180),
    # ])
    # print("Press 'T' to rotate 180 degrees")

    # ######### A "forward" command would go here

    # keycom5 = KeyCommander([
    #     (KeyCode(char='y'), navigator_node.undo_random_rotation),
    # ])
    # print("Press 'Y' to undo the random rotation")

    # # # DEBUG 
    # # keycom6 = KeyCommander([
    # #     (KeyCode(char='q'), navigator_node.rotate_troubleshooting),
    # # ])
    # # print("Press 'q' to move a pre amounrqq")

    # keycom7 = KeyCommander([
    #     (KeyCode(char='n'), navigator_node.send_navigation_goal(0.0, 0.0, 0.0, 0.0, 0.0, 0.0)),
    # ])
    # print("Press 'n' to send a pose to navigator node")


     
	# # Adding each keycom to the executor
    exec.add_node(navigator_node)
    # exec.add_node(keycom2) 
    # exec.add_node(keycom3)
    # exec.add_node(keycom4)
    # exec.add_node(keycom5)
    # # exec.add_node(keycom6)
    # exec.add_node(keycom7)


  
    # Try/Except to shutdown "gracefully"
    try:
        exec.spin()
    except KeyboardInterrupt:
        # stop(navigator_node)
        # keycom2.stop()
        # keycom3.stop()
        # keycom4.stop()
        # keycom5.stop()
        # keycom7.stop()
        rclpy.shutdown() # Added comment

