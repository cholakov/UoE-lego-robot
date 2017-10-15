class Whiskers():
	def __init__(self):
		print("Initializing Whiskers")

class IR():
	def __init__(self):
		print("Initializing IR")

class Sonar():
	def __init__(self):
		print("Initializing Sonar")


class Hall():
	def __init__(self):
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

class Light():
	def __init__(self):
		print("Initializing Light")
