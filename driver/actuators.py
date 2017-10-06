# Accomodate for different power of motors, if necessary

FILTER_LEFT  = 1
FILTER_RIGHT = 1.0

SPEED_MAX 	= 100
SPEED_MED 	= 80
SPEED_LOW 	= 60


class Motors:
	def __init__(self, IO):
		self.IO = IO

	def speed(self, left_motor, right_motor):
		self.IO.setMotors(FILTER_LEFT * left_motor, FILTER_RIGHT * right_motor)

	def go(self, speed="Max"):
		if speed == "Max":
			self.speed(SPEED_MAX, SPEED_MAX)
		elif speed == "Med":
			self.speed(SPEED_MED, SPEED_MED)
		elif speed == "Low":
			self.speed(SPEED_LOW, SPEED_LOW)


	def stop(self):
		print("Stopping")

	def left(self, onSpot=False):
		""" 
		Turn left. 
		Optionally, specify whether to turn on spot (sets speed to 0). 

		"""

	def right(self, onSpot=False):
		""" 
		Turn right. 
		Optionally, specify whether to turn on spot (sets speed to 0). 

		"""

	def scan():
		""" 
		Perform a full 360 degrees scan.

		"""

class Servo:
	def __init__(self, IO):
		self.IO = IO

