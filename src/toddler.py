#!/usr/bin/env python
__TODDLER_VERSION__="1.0.0"

import time
from mission import pathFinder



# Hardware test code
class Toddler:
    def __init__(self,IO):
        print "\nI'm alive!"
        self.IO=IO
        self.IO.servoEngage()
        

    # This is a callback that will be called repeatedly.
    # It has its dedicated thread so you can keep block it.
    def Control(self, OK):
        mission = pathFinder(self.IO, OK)
        # mission.explore()
        mission.pointAntenna(0.48, 3.44, 0)

        ########################################    -- working distance code

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


        print("Done 0.5m")
        self.IO.setMotors(0,0)
##########################################
        
        while OK():
            # print(self.IO.getInputs())
            continue


    def Vision(self, OK):
        while OK():
            continue

# right [0] True
# left [1] True
