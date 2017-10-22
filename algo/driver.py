
from actuators import Motors
from sensors import Hall


class Driver():
	"""
	Driver first receives a map from pathFinder with instructions how to move through space. Then Driver
	coordinates the actuators to execute the task, returning success on completion.
	"""
	def __init__(self, IO, OK):
		"""
		:param route: a dictionary of the path the driver has to follow
		:return:
		"""
		self.IO = IO
		self.OK = OK
		self.motors = Motors(self.IO)
		self.hall = Hall(self.IO)

	def go(self):
		self.motors.go()

	def stop(self):
		self.motors.stop()

	def goTo(self, pose):
		""" 
		Given coordinates, rotate itself to face in that direction.
		Useful for connecting to a satellite.
		:coordinates: (x,y) tuple of target location in the Arena Coordinate System
		:theta: target orientation in the Arena Coordinate Systems
		"""
		x, y, theta = pose
		print(" Going to " + str(pose))

		self.motors.go()
		self.hall.measure(500)
		self.motors.stop()



	def getUnstuck(arena):
		"""
		Recovery procedure after getting stuck.
		:return: success after succesfully getting unstuck

		"""
		print("getUnstuck")

