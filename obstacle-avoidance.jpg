Whisker sensors
Sonar
touch sensors
IR sensors

def avoidance():
	
	set.IO.setMotors(100,100)
	
	
	while nothing is detected:
		go straight
	if something is detected: 
		stop
		turn until obsticale is out of range
		continue straight
	
	stuck: 
		reverse until out of range
		turn 180 
		go straight
	
	Hall effect Sensor:
		 
		 frequency * gear ratio = frequency of wheel
		 (time * frequency of wheel * 2*pi*r) = distance travelled
	
	To turn 90 degrees:
		(2*pi*r)/4 = 2*pi*r*f*t
		find time that the motors need to move for 
import threading
	
	def speedMeasurement():
		speed = f*2*pi*r 
	
	def Control(self, ok):
		measurement_thread = threading.Thread(target=function_that_downloads, args=my_args)
		measurement_thread.start()
		preSetAnalog = []
		preSetDigital = []
		analog = self.IO.getSensors 
		digital = self.IO.getInputs
		if(check sensors reading are in normal range/not normal(too close) AND digital inputs are unchanged):	-- check against preknown array
			sensors = false
		else:
			sensors = true
	while ok():
		while sensors == false:
			self.IO.setMotors(100,100)
			analog = self.IO.getSensors 			
			digital = self.IO.getInputs
			if(sensors increase by certain value/ change to certain range):		-- check analog array values and if they deviate to certain values then we are near an obsticale 
				sensors = true
			elif(digital sensors switch from 0-1/1-0)	-- omit the hall effect sensor from this check
				sensors = true
			
		while(sensors == true):
			self.IO.setMotors(0,0)
			analog = self.IO.getSensors 
			digital = self.IO.getInputs
			while(at least one of the digital sensors change from preset) -- omit the hall effect senor from this check
				hallEffect = digital.split -- get the hall effect sensor and measure with gear ratio to find 0.25m
				turn 90 degrees 
				check sensors
				if(sensors == preSetDigital)
					sensors = false
			while(analog sensors have deviated):
				turn wheels oposite way to the increased values eg( self.IO.setMotors(80,100)/self.IO.setMotors(100,80)
				hallEffect = digital.split -- get the hall effect sensor and measure with gear ratio to find 0.5m
				while hallEffect < value
					self.IO.setMotors(-100,-100) -- reverse 0.5m
			
				if(sensors return to ok range):		-- check analog array values and if they are back in normal range
					sensors = false 
			
			
			
			
