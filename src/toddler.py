#!/usr/bin/env python
__TODDLER_VERSION__="1.0.0"

import time
from mission import pathFinder
import sys



# Hardware test code
class Toddler:
    def __init__(self,IO):
        print "\nI'm alive!"
        self.IO=IO
        self.IO.servoEngage()
        
    def ArgumentList(self,args):

        #turning calibration = sys.argv[1]
        if(len(sys.argv) < 2):
            pass
        else:
            print 'Argument List:', str(sys.argv[1])
            self.motors.calibration = sys.argv[1]

            # Argument 1 is the calibration for turning, eg:
            # In command line: sandbox (calibration), if omitted then calibration is 90
            # Untested due to broken fitpc

    # This is a callback that will be called repeatedly.
    # It has its dedicated thread so you can keep block it.
    def Control(self, OK):
        mission = pathFinder(self.IO, OK)
        # mission.explore()
        mission.pointAntenna(0.48, 3.44, 0)

       
        
        while OK():
            # print(self.IO.getInputs())
            continue


    def Vision(self, OK):
        while OK():
            continue

# right [0] True
# left [1] True
