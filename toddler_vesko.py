#!/usr/bin/env python
__TODDLER_VERSION__="1.0.0"

import time
import numpy
import cv2
import datetime

# Hardware test code
class Toddler:
    def __init__(self,IO):
        print 'I am a toddler playing in a sandbox'
        self.IO=IO
        self.inp=[0, 0, 0, 0, 0, 0, 0, 0]
	self.IO.setMotors(100,100,100,100)

    def move(self, l,r):
      if not l and not r:
        return [0, 0]
      if l and not r:
        return [100, -100]
      if not l and r:
        return [-100, 100]
      if l and r:
        return [100, 100]    
        

    # This is a callback that will be called repeatedly.
    # It has its dedicated thread so you can keep block it.
    def Control(self, OK):
        while OK():
	    self.IO.servoEngage()
	    self.IO.servoSet(100)
	    self.IO.servoSet(150)
	    self.IO.setStatus('flash',2,6,0)

    # This is a callback that will be called repeatedly.
    # It has its dedicated thread so you can keep block it.
    def Vision(self, OK):            
            time.sleep(0.05)
            

        
