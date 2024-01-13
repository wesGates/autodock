# ros2_Create3
A custom auto-docking procedure for a Create3 mobile robot using ROS2 Humble on Ubuntu 22.04 LTS. 

The goal of this project is to make my own auto-docking routine for the Create3 robot. The robot will undock, move to a random location, and then navigate and mount itself to the dock for charging without using the built-in docking function.

My method involves setting a "home" coordinate position directly after undocking, then using the on-board odometry sensor data to navigate back to the home  position after the random movements have been made. After the rough approach to the dock has been made using the odometry information, the IR senors at the front of the robot are used to detect the infra-red cones projected from the docking station to make small adjustments to the robot's speed and heading until the /is_docked topic is "True", indicating a successful dock.
