#// run_roomba
import rclpy
from rclpy.executors import MultiThreadedExecutor

# Garrett packages (Easy program start)
from pynput.keyboard import KeyCode
from key_commander import KeyCommander

# Import the Roomba class from myDock_audiostuff
from Roomba_skeleton import Roomba

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

global_rotation_angle = None

if __name__ == '__main__':
    exec = MultiThreadedExecutor(3)
    exec.add_node(roomba)
    exec.add_node(sensor)

    roomba.chirp(ready_notes)

	# KeyCommander Definitions
    keycom1 = KeyCommander([
        (KeyCode(char='u'), roomba.undock_and_drive),
    ])
    print("Press 'U' to undock and move forward, or to move forward after being undocked")

    keycom2 = KeyCommander([
        (KeyCode(char='r'), roomba.rotate_randomly),
    ])
    print("Press 'R' to rotate randomly")
    print(global_rotation_angle)

    keycom3 = KeyCommander([
        (KeyCode(char='f'), roomba.drive_forward),
    ])
    print("Press 'F' to move forward")

    keycom4 = KeyCommander([
        (KeyCode(char='t'), roomba.rotate_180),
    ])
    print("Press 'T' to rotate 180 degrees")
    
	# Adding each keycom to the executor
    exec.add_node(keycom1)
    exec.add_node(keycom2) 
    exec.add_node(keycom3)
    exec.add_node(keycom4)
    
    # Try/Except to shutdown "gracefully"
    try:
        exec.spin()
    except KeyboardInterrupt:
        keycom1.stop()
        keycom2.stop()
        keycom3.stop()
        rclpy.shutdown() # Added comment