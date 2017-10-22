
# If you see unexpected obstacle in front, stop. Look around with the sonar in what direction to continue.

# Inform mapper that unexpected obstacle has been detected.
# Store in a matrix of temporary obstacles it there until timeout

class obstacleAvoidance():
	def __init__(self, IO, OK):
		"""

		"""
		self.IO = IO
		self.OK = OK

	def on(self):
		print("Obstacle avoidance active.")


	def off(off):
		print("Obstacle avoidance deactivated.")