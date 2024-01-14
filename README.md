# Custom Auto-Docking Procedure for Create3 Robot

This project focuses on developing a custom auto-docking routine for the Create3 mobile robot using ROS2 Humble on Ubuntu 22.04 LTS. The robot is programmed to undock, move to a random location, and then navigate back to its dock for recharging, bypassing the built-in docking function.

## Project Overview

The robot sets a "home" coordinate position after undocking and uses onboard odometry sensor data to navigate back to this position. For precise docking, IR sensors detect infrared cones from the docking station, guiding the robot. The project incorporates auditory signals for troubleshooting and an algorithm to reset the robot if it fails to dock after several attempts.

## Repository Structure

### Scripts Location

The scripts are located in the `src` folder. Here are the key scripts:

1. **Roomba Node Script (`src/roomba_node.py`)**: 
   - **Description**: Manages the robot's actions like undocking, driving, rotating, and docking.

2. **Odometry Node Script (`src/odom_node.py`)**: 
   - **Description**: Publishes the robot's odometry information.

3. **IR Monitor Node Script (`src/ir_monitor_node.py`)**: 
   - **Description**: Monitors and publishes IR sensor data from the robot.

4. **Dock Status Monitor Node Script (`src/dock_status_monitor_node.py`)**: 
   - **Description**: Monitors and publishes the robot's docking status.

5. **Key Commander Script (`src/key_commander.py`)**:
   - **Description**: Facilitates key-triggered callbacks for controlling the robot.

## Key Features

- **Auditory Feedback**: The system uses sound signals to assist in troubleshooting during the robot's operation.
- **Docking Algorithm**: If the robot fails to dock successfully within a certain number of attempts, it resets its position and tries again.

## Installation

1. Install ROS2 Humble on Ubuntu 22.04 LTS.
2. Clone the repository into your ROS2 workspace.
3. In the `src` folder, build the workspace with `colcon build`.
4. Source the workspace environment.

## Usage

Launch the nodes using ROS2 launch files or command line, and use the KeyCommander for interactive control.
