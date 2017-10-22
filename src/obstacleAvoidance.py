# If you see unexpected obstacle in front, stop. Look around with the sonar in what direction to continue.

# Inform mapper that unexpected obstacle has been detected.
# Store in a matrix of temporary obstacles it there until timeout


class InterruptExecution (Exception):
	pass

class obstacleAvoidance():
	def __init__(self, IO):
		self.IO = IO
		print("Obstacle avoidance active.")

	def check(self, sensors, driver):
		# If you see something ahead, turn left until the right IR senses danger from the wall
		if sensors.sonar() == "danger":
			def callback(sensors):
				sensors.update()
				# if sensors.ir("right") == "danger":
				# 	raise (InterruptExecution('Stop turning! Right IR sees a wall!'))
				if sensors.sonar != "danger":
					raise (InterruptExecution('Stop turning! Opening ahead'))
			driver.motors.turnUntil("left", callback, InterruptExecution, sensors)


		if sensors.ir("left") == "danger":
			def callback(sensors):
				sensors.update()
				if sensors.ir("left") != "danger":
					raise (InterruptExecution('Stop turning! Left IR sees a wall!'))
			driver.motors.turnUntil("right", callback, InterruptExecution, sensors)

		if sensors.ir("right") == "danger":
			def callback(sensors):
				sensors.update()
				if sensors.ir("right") != "danger":
					raise (InterruptExecution('Stop turning! Right IR sees a wall!'))
			driver.motors.turnUntil("left", callback, InterruptExecution, sensors)








