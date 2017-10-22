class Hall():
	def __init__(self, IO):
		self.IO = IO
		self.DEFINITION = 17.8 # centimeters covered between two signals from the hall effect

	def measure(self, distance):
		"""
		Measure distance
		:param distance: in cm how much distance you want to cover
		:return:
		"""
		# 5.6 signals from the hall effect per meter, or 17.8 cm per signal

		# rotations = (distance / (2*np.pi*0.041))      #radius of the wheel = 4.1cm = 0.041m, gearRatio = 0.4
		# rotations = rotations / 0.4
		# rotations = (2*rotations) /3

		rotations = distance / self.DEFINITION

		while rotations > 0 :
			digital = self.IO.getInputs()
			if digital[7] :        #if the hall effect value is true
				rotations = rotations - 1   # take one rotation off
			while digital[7]:
				pass

class Sensors():
	def __init__(self, IO):
		self.IO = IO

		self.ports = {
			"light": {},
			"sonar": None,
			"ir" :	 {}
		}
		self.thresholds = {
			"light": {},
			"sonar": None,
			"ir" :	 {}
		}
		self.readings = {
			"light": {},
			"sonar": {},
			"ir" :	 {}
		}

		self.ports["sonar"] = 0
		self.ports["ir"]["left"] = 1
		self.ports["ir"]["right"] = 2
		self.ports["light"]["left"] = 5
		self.ports["light"]["right"] = 6

		self.thresholds["light"]["left"] = [220, 450]		# Provide exactly two values
		self.thresholds["light"]["right"] = [100, 265]		# Provide exactly two values
		self.thresholds["sonar"] = 20
		self.thresholds["ir"]["left"] = 390
		self.thresholds["ir"]["right"] = 385

	def update(self):
		analog = self.IO.getSensors()
		digital = self.IO.getInputs()

		# Update Readings
		self.readings["sonar"] = analog[self.ports["sonar"]]
		self.readings["light"]["left"] = analog[self.ports["light"]["left"]]
		self.readings["light"]["right"] = analog[self.ports["light"]["right"]]
		self.readings["ir"]["left"] = analog[self.ports["ir"]["left"]]
		self.readings["ir"]["right"] = analog[self.ports["light"]["right"]]

	def light(self):
		ground = None
		if self.readings["light"]["left"] > self.thresholds["light"]["left"][1]:
			ground = "silver"
		elif self.readings["light"]["left"] < self.thresholds["light"]["let"][0]:
			ground = "black"
		else:
			ground = "grey"
		return ground

	def sonar(self):
		if self.readings["sonar"] < self.thresholds["sonar"]:
			print ('Sonar dangerously close.')
			return "danger"
		else:
			return self.readings["sonar"]

	def ir(self, side):
		if side == "left":
			if self.readings["ir"]["left"] < self.thresholds["ir"]["left"]:
				print ('Left IR dangerously close.')
				return "danger"
			else:
				return self.readings["ir"]["left"]

		elif side == "right":
			if self.readings["ir"]["right"] < self.thresholds["ir"]["right"]:
				print ('Right IR dangerously close.')
				return "danger"
			else:
				return self.readings["ir"]["right"]


	# random location
	# 175 84
	# 187 75
	# 166, 74
	# 163, 70
	#
	# docking station
	# 303 130
	# 294 130
	# 291, 131
	#
	# reflective tape
	# 655 512
	# 638 394