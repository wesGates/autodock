def takeoff(self):
		"""
		This function undocks, drives out a prescribed distance, rotates randomly,
		drives a prescribed distance, then returns itself to a position to prepare for 
		docking
		"""
		self.chirp(start_note)
		self.reset_pose()

		# Read current dock status
		self.sensor.poll()

		### Undock ###
		self.chirp(start_note)
		self.undock_ac.wait_for_server() # Wait till its ready
		undock_goal = Undock.Goal() # Make goal
		self.undock_ac.send_goal_async(undock_goal) # Send goal blocking


		### Drive out a prescribed distance from being undocked ###
		self.drive_amount(distance_1)
		# Read current dock status
		self.sensor.poll()
		self.reset_pose()
		
		### Random rotation ###
		self.reset_pose()
		self.chirp(rand_note)

		random_angle = random.uniform(-pi, pi)
		print("Rotating randomly by angle:", random_angle)

		# Store the random r0tation angle for future use
		self.last_rotation_angle = random_angle

		# Create and send the goal
		self.rotate_ac.wait_for_server()
		rotate_goal = RotateAngle.Goal()
		rotate_goal.angle = random_angle 
		self.rotate_ac.send_goal_async(rotate_goal)
		self.chirp(rand_note)
		print("Rotating randomly by angle:", random_angle)


		############# The following functions will be removed once the robot 
		# has docked succesfully with this handicap
		
		### Drive prescribed distance ###
		self.chirp(start_note)
		self.drive_amount(distance_2)

		### Rotate 180 degrees ###
		rotate_angle = pi
		self.rotate_amnt = (pi)

		### Drive prescribed distance ###
		self.chirp(start_note)
		self.drive_amount(distance_2)

		### Undo random rotation to align with the dock ###
		self.rotate_amnt(-random_angle)


### Next steps: 
# "
# Move forward slowly while polling the IROpcode 161 (the force field). Once
# conctact has been made with the force field, stop the robot and initiate
# the docking sequence using the ir_opcode_callback function to help the robot 
# make adjustments during the approach. This docking function will need to 
# be polling the docking sensor for /is_docked = True, at which point the robot 
# will stop moving. 
# "

# Alternatively (and best) the robot will start the docking sequenc after having performed
# THe random rotation and drive-out actions. 

# TODO: 
# Add the nodes for the forcefield sensor (optional)
# Test if all the functions work as written
### If they work, remove: 
# undock_and_drive
# drive_forward
# rotate_180
# rotate_troubleshooting


# TODO: Once the robot has been shown to be able to dock, remove: 
# undo_random_rotation
# rotate_randomly