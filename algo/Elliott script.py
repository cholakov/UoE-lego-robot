import numpy as np
import time
import cv2

# Main Toddler class
class Toddler:
    # Initialiser
    def __init__(self,IO):
        # Print a message
        print 'I am a toddler playing in a sandbox'
        # Store the instance of IO for later
        self.IO=IO
        self.IO.servoEngage()
        # Add more initialisation code here

    # This is a callback that will be called repeatedly.
    # It has its dedicated thread so you can keep blocking it.

######################################################
    def Turn(self,angle):
        t = (float(angle)/90) * 2.125

        start = time.time()
        end = time.time()
        while end - start < t:

            self.IO.setMotors(-60,60)
            end = time.time()
        self.IO.setMotors(0,0)


    def antenna(self,o,a):
        calibration = 7
        self.IO.servoSet(0)
        time.sleep(1.0)
        angle = np.arctan(o/a)
        angle = np.rad2deg(angle)
        self.IO.servoSet(int(angle) - calibration)    # bit off because of the gear ratio, maybe -4

    def distance(self,distance):    # random time test method

        t = 2

        start = time.time()
        end = time.time()
        while end - start < t:
            print (end-start)
            self.IO.setMotors(60,60)
            end = time.time()
        self.IO.setMotors(0,0)


    def Control(self, OK):

        self.Turn(90)
        self.antenna(1.25,0.9)
        self.distance(20)
        while OK():
            pass
        
#####################################################


    # This is a callback that will be called repeatedly.
    # It has its dedicated thread so you can keep blocking it.
    def Vision(self, OK):
        while OK():
            # Add vision code here
            time.sleep(0.05)



