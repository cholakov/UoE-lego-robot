
# If you see unexpected obstacle in front, stop. Look around with the sonar in what direction to continue.

# Inform mapper that unexpected obstacle has been detected.
# Store in a matrix of temporary obstacles it there until timeout

class obstacleAvoidance():
	def __init__(self, IO):
		print("Obstacle avoidance active.")

	def on(self, sensors, driver):
		if sensors.sonar() == "danger":
			driver.motors.turn(45, "right", True)

		if sensors.ir("left") == "danger":
			driver.motors.turn(45, "left", True)

		if sensors.ir("right") == "danger":
			driver.motors.turn(45, "right", True)



