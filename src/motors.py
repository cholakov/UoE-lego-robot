import time

class Motors:
	def __init__(self, IO):
		self.IO = IO
		self.speed = 90
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
		print("[MOTORS] Going straight ahead.")
		self.IO.setMotors(self.speed*self.FILTER_RIGHT,self.speed*self.FILTER_LEFT)

	def back(self):
		print("[MOTORS] Backing up.")
		self.IO.setMotors(-self.speed*self.FILTER_RIGHT,-self.speed*self.FILTER_LEFT)

	def turn(self, angle, direction, onSpot=False):
		""" 
		Turn to a specified angle. 
		Positive numbers turn right.
		Negative numbers turn left.
		Optionally, specify whether to turn on spot (sets speed to 0). 

		"""

		print("[MOTORS] Turning {0} degrees {1}.".format(angle, direction))
		calibration = 95	# when you ask it to turn 90 how many degrees does it go
		angle = (90/float(calibration)*float(angle))
		t = (float(angle)/90) * 2.125	# 2.125 is the time it takes to turn 90 degrees
		start = time.time()
		end = time.time()
		if onSpot:
			while end - start < t:
				self._turn(direction)
				end = time.time()
			self.stop()
		else:
			self.stop()
			while end - start < t:
				self._turn(direction)
				end = time.time()
			self.go()

	def measure(self,distance):
		

        	distance = 0.5
       		filterLeft = 1.0
        	filterRight = 0.7


       		self.IO.setMotors(60*filterLeft , 60*filterRight)

        	t = distance/0.24   # equation is y = 22.8x but using 24 take rolling into account


        	end = time.time()


        	rotations = distance / 0.103044239

        	start = time.time()

        	while rotations > 0 and (end-start <t):  #if there are still rotations left and there is time still left
          		end = time.time()


            	digital = self.IO.getInputs()
            	if digital[7] :        #if the hall effect value is true
                	rotations = rotations - 1   # take one rotation off
            	if rotations < 1 and (end-start) < t:
                	print("Stopped at break point")
                	break
            	while digital[7]:
                	pass


        	print("Done")
        	self.IO.setMotors(0,0)

        
		
	def turnUntil(self, direction, callback, InterruptExecution, *param):
		"""
		Turn until callback function raises exception.

		"""
		while True:
			self._turn(direction)
			time.sleep(0.5)
			try:
				callback(*param)
			except InterruptExecution:
				self.go()
				break

	def stop(self):
		print("[MOTORS] Stopped.")
		self.IO.setMotors(0,0)

	def scan360():
		""" 
		Perform a full 360 degrees scan.

		"""
