

class Motors:
	def __init__(self, IO):
		self.IO = IO
		self.speed = 40
		# Accommodate for different power of motors.
		# In line of movement (with the battery ahead), the left motor is faster.
		# In the IO tuple, the left motor is the second value.
		self.FILTER_RIGHT = 1.0
		self.FILTER_LEFT = 0.70

	def go(self):
		self.IO.setMotors(self.speed*self.FILTER_RIGHT,self.speed*self.FILTER_LEFT)

	def back(self):
		self.IO.setMotors(-self.speed*self.FILTER_RIGHT,-self.speed*self.FILTER_LEFT)

	def left(self, onSpot=True):
		""" 
		Turn left. 
		Optionally, specify whether to turn on spot (sets speed to 0). 

		"""

	def right(self, onSpot=True):
		""" 
		Turn right. 
		Optionally, specify whether to turn on spot (sets speed to 0). 

		"""

	def stop(self):
		print("Stopping")
		self.IO.setMotors(0,0)


	def scan360():
		""" 
		Perform a full 360 degrees scan.

		"""

class Servo:
	def __init__(self, IO):
		self.IO = IO