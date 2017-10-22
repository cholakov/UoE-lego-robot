#!/usr/bin/env python
__TODDLER_VERSION__="1.0.0"

import time
from algo.pathFinder import pathFinder



# Hardware test code
class Toddler:
    def __init__(self,IO):
        print "Hey, I'm alive!"
        self.IO=IO
        

    # This is a callback that will be called repeatedly.
    # It has its dedicated thread so you can keep block it.
    def Control(self, OK):
        mission = pathFinder(self.IO, OK)
        mission.explore()

    def Vision(self, OK):
        while OK():
        	continue