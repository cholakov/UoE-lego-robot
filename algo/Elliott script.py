import numpy as np
import time
import cv2

# Main Toddler class
class Toddler:
    # Initialiser
    def __init__(self,IO):
        # Print a message
        print "Hey, I'm alive!"
        # Store the instance of IO for later
        self.IO=IO
        self.IO.servoEngage()
        rotations = 0


    def Hall(self,distance,direction):
        if direction == "forth":
            self.IO.setMotors(30,40)          # 1=forward, 2=backwards
        elif direction == "back":
            self.IO.setMotors(-100,-100)

        # num of rotations to cover 1 meter distance
        rotations = (distance / (2*np.pi*0.041))      #radius of the wheel = 4.1cm = 0.041m, gearRatio = 0.4
        rotations = rotations / 0.4
        rotations = (2*rotations) / 3

        rotations  = 5.6
        while rotations > 0 :
            digital = self.IO.getInputs()
            if digital[7] :        #if the hall effect value is true
                rotations = rotations - 1
            # Ignore consecutive True readings from hall effect, until at least one False reading
            # This is necessary because Hall sends 2-3 True readings one after another which screws up the interpretation
            while digital[7]:
                pass

            print rotations

        self.IO.setMotors(0,0)		#stop motors after movement

    def HallAngle(self,angle):
        self.IO.setMotors(100,-80)
        distance = (2*np.pi*0.19) / (360/angle)
        rotations = (distance / (2*np.pi*0.041)) / 0.4

        while rotations>0:
            digital = self.IO.getInputs()
            print digital
            if digital[7]:
                print rotations
                rotations = rotations -1
            while digital[7]:
                pass

            print rotations
        self.IO.setMotors(0,0)


    def satilliteFinder(self,opposite,adjacent):

         self.IO.servoSet(0)
         time.sleep(1.0)
         position = np.arctan(opposite/adjacent)
         position =np.rad2deg(position)
         print position
         self.IO.servoSet(position)


    def Control(self, OK):
        self.Hall(1, "forth")
        #self.HallAngle(90,1.25,0.64)
        while OK():
            continue

    def Vision(self, OK):
        while OK():
            continue