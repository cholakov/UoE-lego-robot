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

       
        
        while OK():
            # print(self.IO.getInputs())
            continue


    def Vision(self, OK):
        while OK():
            continue

# right [0] True
# left [1] True
