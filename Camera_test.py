#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 19:52:30 2020

@author: pi
"""

from picamera import PiCamera
from time import sleep
#import cv2

camera = PiCamera()
camera.start_preview()
sleep(2)
#camera.capture('/home/pi/Desktop/test.jpg')
#camera.start_recording('/home/pi/Desktop/test.jpg')
camera.start_recording('/home/pi/Desktop/video_test.h264')
sleep(10)
camera.stop_recording()
camera.stop_preview()
camera.close()