import time
import numpy
import cv2
import numpy as np
import sys

# Main Toddler class
class Toddler:
	# Initialiser
	def __init__(self,IO):
		# Print a message
		print 'I am a toddler playing in a sandbox'
		# Store the instance of IO for later
		self.IO=IO
		self.IO._interfaceKit.setSensorChangeTrigger(0,0)

		# Add more initialisation code here

		# This is a callback that will be called repeatedly.
		# It has its dedicated thread so you can keep blocking it.
		self.POI = 0    # number of POI's we have hit
		self.position = [(1.45,1.05,90),(-0.1,3.05,180),(-0.85,1.80,270)]   #hard coded position
		self.q = 12    #turn loop variable, 21 for stashed batteries
		self.recentTurn = 0    #most recent turn angle
		self.d = 'left'    #most recent turn direction


		self.x_distance = [] #sum to find x coordinate
		self.y_distance = [] #sum to find y coordinate
		self.timeStampList = []  #time since last poll
		self.timeOnPOI = [] #time spent on POI
		self.newLeg = False
		self.leg = 0    # leg we are on
		self.highways = [1.4,3.45,2.40,2.00,1.50,2.00,1.40,2.00,1.50,2.00,1.40,2.00,1.50,2.00,1.40,2.00]   #highway length
		self.POIDistance = 0    #distance to POI on current leg
                self.justVisitedPOI = False
                self.lastPOItime = time.time()


	def pushDistance(self,distance,leg):
		print "Pushing Distance"
		leg = self.leg

		  #On horizonal
		if leg == 0 or leg == 4:
			print "Leg 0 or 4, X pushed:  ",distance
			self.x_distance.append(distance)  #+x
		elif leg == 2:
			print "Leg 2, X pushed:  ",distance
			self.x_distance.append(-distance)  #-x
		elif leg ==1 or leg == 5:
			print "Leg 1 or 5, y pushed:  ",distance
			self.y_distance.append(distance) #+y
		elif leg == 3:
			print "Leg 3, y pushed:  ",distance
			self.y_distance.append(-distance) #-y



	def distance_moved(self,newLeg,POI):   #newLeg -- boolean, POI -- boolean
	#POI is true when we have hit a POI

		if POI:
			print "Hit POI"

			self.timeStampList.append(time.time())
			self.timeOnPOI.append(time.time())

			timetaken = self.timeStampList[-1] - self.timeStampList[0]
			print "Timetaken",timetaken
			distance = 0.24 * timetaken

			self.POIDistance = distance
			print "Distance to POI on leg: ",distance


			## after the robot has moved forward and back after turning the antenna push time to timeOnPOI[]

		if newLeg:  #if we have stated a new leg append timestampList
			print "New Leg"

			distance = self.highways[self.leg-1]
			print "Distance of leg just covered: ",distance

			self.pushDistance(distance,self.leg-1)   # push distance to previous leg

			print "TimeStampList size BEFORE zeroing" ,np.size(self.timeStampList)

			self.timeStampList = []

			print "TimeStampList size AFTER zeroing" ,np.size(self.timeStampList)

			self.timeOverPOI = []
			self.timeStampList.append(time.time())
			self.newLeg = False  # Only true when we turn90


	def calculatePosition(self):    #no inputs as uses global variables
		print "calculate Position"
		leg = self.leg-1

		X = np.sum(self.x_distance)
		y = np.sum(self.y_distance)

		if leg == 0 or leg == 4:
			print "Leg 0 or 4: "
			X = np.sum(self.x_distance) + self.POIDistance
		elif leg == 2:
			print "Leg 2: "
			X = np.sum(self.x_distance) - self.POIDistance
		  #on vertical
		elif leg == 1 or leg == 5:
			print "Leg 1 or 5: "
			y = np.sum(self.y_distance) + self.POIDistance
		elif leg == 3 :
			print "Leg 3: "
			y = np.sum(self.y_distance) - self.POIDistance


		theta = self.leg * 90
		print "Print X,y,theta: ",np.absolute(X),np.absolute(y),theta
		return np.absolute(X),np.absolute(y),theta


	#def pointAntenna(self,robot_x, robot_y, theta):
	def pointAntenna(self):
		"""
		  o: opposite (height ground to ceiling)
		  a: adjacent (distance from location of the robot to the projection of the satellite on the ground)

		  """
		#robot_x,robot_y,theta = self.calculatePosition()
		#direction = 'left'
		#robot_x,robot_y,theta = self.position[self.POI]
		robot_x,robot_y,theta = self.calculatePosition()
		print "Aligning antenna"
		satellite_x = -0.69
		satellite_y = 0

		x = np.arctan((robot_y - satellite_y) / (robot_x - satellite_x))
		x = np.rad2deg(x)
		p = 180 - 90 - x  # calculate residual angle to move after theta and 90 have been moved. Direction based on position relative to satellite



		if (robot_x > satellite_x):
		    distance = theta + 90 + p
		    distance = 360 - distance
		    self.turnPOI('left',distance)
		    self.recentTurn = distance
		    self.d = 'right'
		else:                             ################## double check these methods
		    distance =  theta + x
		    #self.turnPOI('left',distance)
		    self.recentTurn = distance
		    self.d = 'right'

		o = 2.95
		calibration = 7

		a = np.power((robot_y - satellite_y),2) + np.power((satellite_x - robot_x),2)
		a = np.sqrt(a)
		self.IO.servoEngage()
		self.IO.servoSet(0)
		time.sleep(1.0)
		angle = np.arctan(o / a)
		angle = np.rad2deg(angle)
		self.IO.servoSet(int(angle) - calibration)  # bit off because of the gear ratio = 7

		print("Pointed antenna at angle " + str(angle))
		self.POI +=1
		time.sleep(10)
		self.IO.servoSet(0)

		print "Turning back"

		self.turnPOI(self.d,self.recentTurn)


		filterLeft = 1.0
		filterRight = 0.7

		self.IO.setMotors(filterRight*70,filterLeft*70)
                self.lastPOItime = time.time()

	  #return (distance,direction)



	def turnPOI(self,direction,angle):    #only used when turning towards POI and back


	    filterLeft = 1.0
	    filterRight = 0.7
	    print "Turning: ",angle

	    q = int(round(float(angle)/(90.0/float(self.q))))
	    print q

	    t = 2.125 + (0.05*45)	# 2.125 is the time it takes to turn 90 degrees
	    start = time.time()
	    end = time.time()
            if direction == 'left':
	        for i in range(q-2):
	            time.sleep(0.25)
	    	    self.IO.setMotors(0,0)
	   	    time.sleep(0.15)
                    self.IO.setMotors(filterRight*-100,filterLeft*100) #left
                    end = time.time()
		    if start - end > t:
	                break
            if direction == 'right':
	        for i in range(q+1):
	            time.sleep(0.25)
	    	    self.IO.setMotors(0,0)
	   	    time.sleep(0.15)
                    self.IO.setMotors(filterRight*100,filterLeft*-100) #left
                    end = time.time()
		    if start - end > t:
	                break
            self.IO.setMotors(0,0)




	def turn90(self):   #only used to turn 90 degrees, needs to update x_distance etc

		print "Turning 90"

		self.IO.setMotors(0,0)

		filterLeft = 1.0
		filterRight = 0.7

		t = 2.125 + (0.05*45)	# 2.125 is the time it takes to turn 90 degrees
		start = time.time()
		end = time.time()
		for i in range(self.q):
		    time.sleep(0.25)
		    self.IO.setMotors(0,0)
		    time.sleep(0.15)
		    self.IO.setMotors(filterRight*-100,filterLeft*100) #left
		    end = time.time()
		    if start - end > t:
		        break

                self.IO.setMotors(0,0)
		time.sleep(0.5)
		self.newLeg = True
		self.leg +=1




	def measure(self, distance):
	    print "We're off"

	    LF = 1.0
	    RF = 0.75

	    self.IO.setMotors(70*RF,70*LF)


	    t = distance/0.24   # equation is y = 22.8x but using 24 take rolling into account


	    rotations = distance / 0.103044239
	    print "Rotations: ",rotations

	    start = time.time()
	    end = time.time()

	    while rotations > 0 and (end-start <t):  #if there are still rotations left and there is time still left, test with or
	        end = time.time()


	        digital = self.IO.getInputs()
		if digital[7] :        #if the hall effect value is true
                    rotations = rotations - 1   # take one rotation off
		if rotations < 1 and (end-start) < t:
		    print("Stopped at break point")
		    break
		while digital[7]:
	    	    pass


	    self.IO.setMotors(0,0)
	    print "Done 1m"






	def Control(self, OK):


		filterLeft = 1.0
		filterRight = 0.7

		onPOI = False


		self.timeStampList.append(time.time())





		while OK():
			self.IO._motorControlI2C.write(chr(2<<5|24|2<<1)+chr(0xff))
			self.IO.setMotors(filterRight*70,filterLeft*70)

			analog = self.IO.getSensors()

			kill = self.IO.getInputs()[0]
			if kill:
				self.IO.setMotors(0,0)
				sys.exit()
				break

			IR_R = self.IO.getSensors()[2]
			if IR_R < 130:
				self.IO.setMotors(70,0)
				time.sleep(0.05)
				self.IO.setMotors(70,70)
			if IR_R > 150:
				self.IO.setMotors(0,70)
				time.sleep(0.05)
				self.IO.setMotors(70,70)

			if analog[1] > 165:
				print"IR activated, initiate turn"
				self.turn90()
				self.distance_moved(self.newLeg,False)

                        if time.time() - self.lastPOItime < 5:
                             analog[3] = 0
                             analog[4] = 0
                             analog[5] = 0

                        if analog[3] < 86 and analog[4] < 86 and analog[5] < 193:
                            self.justVisitedPOI = False


		  	if analog[3] > 86 or analog[4] > 86 or analog[5]>193:
                            if not self.justVisitedPOI:
                                self.justVisitedPOI = True

			        print("Light Sensors: Left {}\tRight {}\tCenter {}".format(analog[3] > 86,analog[4] > 85,analog[5] > 193))
		                self.IO.setMotors(0,0)

                                print "just visited POI", self.justVisitedPOI
			        print "Found POI, initiate turn"
			        self.distance_moved(self.newLeg,True)
			        self.pointAntenna() #pointAntenna when we find a POI
			        #self.timeOnPOI.append(time.time())
			        self.IO.setMotors(filterRight*70,filterLeft*70)





	# This is a callback that will be called repeatedly.
	# It has its dedicated thread so you can keep blocking it.
	def Vision(self, OK):
		while OK():
			# Add vision code here
			time.sleep(0.05)
