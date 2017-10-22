import time

class Motors:
	def __init__(self, IO):
		self.IO = IO
		self.speed = 50
		# Accommodate for different power of motors.
		# In line of movement (with the battery ahead), the left motor is faster.
		# In the IO tuple, the left motor is the second value.
		self.FILTER_RIGHT = 1.0
		self.FILTER_LEFT = 1

	def _turn(self, direction):
		"""
		Implemetns a private turning class.
		:param direction: left or right
		:return:

		"""
		if direction == "left":
			self.IO.setMotors(-self.speed*self.FILTER_RIGHT, self.speed*self.FILTER_LEFT)
		elif direction == "right":
			self.IO.setMotors(self.speed*self.FILTER_RIGHT, -self.speed*self.FILTER_LEFT)

	def go(self):
		print("Going straight ahead.")
		self.IO.setMotors(self.speed*self.FILTER_RIGHT,self.speed*self.FILTER_LEFT)

	def back(self):
		self.IO.setMotors(-self.speed*self.FILTER_RIGHT,-self.speed*self.FILTER_LEFT)

	def turn(self, angle, direction, onSpot=True):
		""" 
		Turn to a specified angle. 
		Positive numbers turn right.
		Negative numbers turn left.
		Optionally, specify whether to turn on spot (sets speed to 0). 

		"""

		print("Turning {0} degrees {1}".format(angle, direction))

		calibration = 90	# when you ask it to turn 90 how many degrees does it go
		angle = (90/calibration*angle)
		t = (float(angle)/90) * 2.125	# 2.125 is the time it takes to turn 90 degrees
		start = time.time()
		end = time.time()
		if onSpot==True:
			self.stop()
			while end - start < t:
				self._turn(direction)
				end = time.time()
			self.go()
		else:
			while end - start < t:
				self._turn(direction)
				end = time.time()


	def turnUntil(self, direction, callback, InterruptExecution, *param):
		"""
		Turn until callback function raises exception.

		"""
		while True:
			self._turn(direction)
			time.sleep(0.75)
			try:
				callback(*param)
			except InterruptExecution:
				self.go()
				break

	def stop(self):
		print("Stopping.")
		self.IO.setMotors(0,0)

	def scan360():
		""" 
		Perform a full 360 degrees scan.

		"""
		
class Servo:
	def __init__(self, IO):
		self.IO = IO