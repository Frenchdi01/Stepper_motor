#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 19:52:30 2020

@author: pi
"""

from picamera import PiCamera
from time import sleep
import cv2

camera = PiCamera()
camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/test2.jpg')
camera.stop_preview()
camera.close()