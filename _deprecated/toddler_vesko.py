#!/usr/bin/env python
__TODDLER_VERSION__="1.0.0"

import time
import numpy
import cv2
import datetime

sonar = [12, 14, 15, 20, 27, 35]
distance = [18.5, 22, 25.5, 32.5, 42, 51.5]

# Hardware test code
class Toddler:
    def __init__(self,IO):
        print 'I am a toddler playing in a sandbox'
        self.IO=IO



    # This is a callback that will be called repeatedly.
    # It has its dedicated thread so you can keep block it.
    def Control(self, OK):
        while OK():
            # self.IO.servoEngage()
            # self.IO.servoSet(100)
            # self.IO.servoSet(150)
            # self.IO.setStatus('flash',2,6,0)
            # self.IO.setMotors(100,100,100,100)
            self.IO._interfaceKit.setSensorChangeTrigger(0,0)
            analog = self.IO.getSensors()
            digital = self.IO.getInputs()
            print(analog)


    # This is a callback that will be called repeatedly.
    # It has its dedicated thread so you can keep block it.
    def Vision(self, OK):            
            time.sleep(0.05)