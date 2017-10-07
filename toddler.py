#!/usr/bin/env python
__TODDLER_VERSION__="1.0.0"

from interface import config

from algorithms.pathFinder import goHome, goTo, explore


# Hardware test code
class Toddler:
    def __init__(self,IO):
        print 'I am a toddler playing in a sandbox'
        self.IO=IO
        self.inp=[0, 0, 0, 0, 0, 0, 0, 0]
        

    # This is a callback that will be called repeatedly.
    # It has its dedicated thread so you can keep block it.
    def Control(self, OK):
    	while OK():
        	print("In Control")


goTo(config.arena, (7,2), (26,8))