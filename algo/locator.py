class Locator:
	def __init__(self):
		print("Localization in progress.")
		self.x = None
		self.y = None
		self.theta = None

	def set(self, x, y, theta):
		self.x = x
		self.y = y
		self.theta = theta

	def pose(self):
		"""
		:return: (x,y,theta) in relation to the Arena Coordinate System
		"""

		# obviously very dummy at this point
		return((self.x, self.y, self.theta))