#!/usr/bin/env python
__TODDLER_VERSION__="1.0.0"

from algo.pathFinder import pathFinder


# Hardware test code
class Toddler:
    def __init__(self,IO):
        print "Hey, I'm alive!"
        self.IO=IO
        

    # This is a callback that will be called repeatedly.
    # It has its dedicated thread so you can keep block it.
    def Control(self, OK):

        # mission = pathFinder(self.IO)
        # mission.origin = (1,1,0)
        # mission.target = (1,10,0)
        # mission.explore()

    	while OK():
            analog = self.IO.getSensors()
            print(analog)

    def Vision(self, OK):
        while OK():
        	continue


# goTo(config.arena, (7,2), (26,8))