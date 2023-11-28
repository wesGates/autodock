#// run_roomba
import rclpy
from rclpy.executors import MultiThreadedExecutor

# Garrett packages (Easy program start)
from pynput.keyboard import KeyCode
from key_commander import KeyCommander

# Import the Roomba class from myDock_audiostuff
from Roomba_skeletonv2 import Roomba

# Your ROS Node packages 
from check_sensor import DockStatusPublisher

# Initialize the ROS client library, namespace, sensor, and class
rclpy.init()
namespace = 'create3_0561'
sensor = DockStatusPublisher(namespace)
roomba = Roomba(namespace, sensor)

# Imports for AudioNote & Chirps
from std_msgs.msg import Header
from builtin_interfaces.msg import Duration
from irobot_create_msgs.msg import AudioNote, AudioNoteVector

# Ready chirp
ready_notes = [
	AudioNote(frequency=583, max_runtime=Duration(sec=0, nanosec= 50000000)),
	AudioNote(frequency=784, max_runtime=Duration(sec=0, nanosec=100000000))
]


if __name__ == '__main__':
    exec = MultiThreadedExecutor(4)
    exec.add_node(roomba)
    exec.add_node(sensor)

    roomba.chirp(ready_notes)

    # Consolidated KeyCommander Definitions
    keycom = KeyCommander([
        (KeyCode(char='u'), roomba.undock_and_drive),
        (KeyCode(char='r'), roomba.rotate_randomly),
        (KeyCode(char='f'), roomba.drive_forward),
        (KeyCode(char='t'), roomba.rotate_180),
        (KeyCode(char='y'), roomba.undo_random_rotation),
        (KeyCode(char='q'), roomba.rotate_troubleshooting),
    ])

    # Print Statements for Key Bindings
    print("Press 'U' to undock and move forward, or to move forward after being undocked")
    print("Press 'R' to rotate randomly")
    print("Press 'F' to move forward")
    print("Press 'T' to rotate 180 degrees")
    print("Press 'Y' to undo the random rotation")
    print("Press 'q' for rotate troubleshooting")

    # Adding keycom to the executor
    exec.add_node(keycom)

    # Try/Except to shutdown "gracefully"
    try:
        exec.spin()
    except KeyboardInterrupt:
        keycom.stop()
        rclpy.shutdown()