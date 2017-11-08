class Hall():
	def __init__(self, IO):
		self.IO = IO
		self.DEFINITION = 17.8 # centimeters covered between two signals from the hall effect

	def measure(self, distance):
		
        distance = 0.5
        filterLeft = 1.0
        filterRight = 0.7


        self.IO.setMotors(60*filterLeft , 60*filterRight)

        t = distance/0.24   # equation is y = 22.8x but using 24 take rolling into account


        


        rotations = distance / 0.103044239

        start = time.time()
	end = time.time()

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


        print("Done 0.5m")
        self.IO.setMotors(0,0)

class Sensors():
	def __init__(self, IO):
		self.IO = IO

		self.ports = {
			"light": {},
			"sonar": None,
			"ir" :	 {},
			"whiskers": {}
		}
		self.thresholds = {
			"light": {},
			"sonar": None,
			"ir" :	 {}
		}
		self.readings = {
			"light": {},
			"sonar": {},
			"ir" :	 {},
			"whiskers": {}
		}

		self.ports["sonar"] = 0
		self.ports["ir"]["left"] = 1
		self.ports["ir"]["right"] = 2
		self.ports["light"]["left"] = 4
		self.ports["light"]["right"] = 5
		self.ports["whiskers"]["left"] = 3
		self.ports["whiskers"]["right"] = 6

		# change sonar threshold to be more sensitive
		self.IO._interfaceKit.setSensorChangeTrigger(self.ports["sonar"],0)

		self.thresholds["light"]["left"] = [220, 380]		# Provide exactly two values
		self.thresholds["light"]["right"] = [100, 181]		# Provide exactly two values
		self.thresholds["sonar"] = 20
		self.thresholds["ir"]["left"] = 500
		self.thresholds["ir"]["right"] = 500

	def update(self):
		analog = self.IO.getSensors()
		digital = self.IO.getInputs()

		# Update Readings
		self.readings["sonar"] = analog[self.ports["sonar"]]
		self.readings["light"]["left"] = analog[self.ports["light"]["left"]]
		self.readings["light"]["right"] = analog[self.ports["light"]["right"]]
		self.readings["ir"]["left"] = analog[self.ports["ir"]["left"]]
		self.readings["ir"]["right"] = analog[self.ports["ir"]["right"]]
		self.readings["whiskers"]["left"] = digital[self.ports["whiskers"]["left"]]
		self.readings["whiskers"]["right"] = digital[self.ports["whiskers"]["right"]]

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

	def ir(self, side, raw=False):
		if side == "left":
			if self.readings["ir"]["left"] > self.thresholds["ir"]["left"]:
				print ('Left IR dangerously close ' + str(self.readings["ir"]["left"]))
				if raw:
					return self.readings["ir"]["left"]
				else:
					return "danger"
			else:
				return self.readings["ir"]["left"]

		elif side == "right":
			if self.readings["ir"]["right"] > self.thresholds["ir"]["right"]:
				print ('Right IR dangerously close ' + str(self.readings["ir"]["right"]))
				if raw:
					return self.readings["ir"]["right"]
				else:
					return "danger"
			else:
				return self.readings["ir"]["right"]

	def whiskers(self, which):
		if which == "left":
			if self.readings["whiskers"]["left"]:
				print("Left whisker waaaaa!")
			return self.readings["whiskers"]["left"]
		elif which == "right":
			if self.readings["whiskers"]["right"]:
				print("Right whisker ddddd huurts!")
			return self.readings["whiskers"]["right"]


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
