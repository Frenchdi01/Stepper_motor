#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 19:52:30 2020

@author: pi
"""

from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep
import cv2
import numpy as np

camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 10

# Generates a 3D RGB array and stores it in rawCapture
raw_capture = PiRGBArray(camera, size=(640, 480))

tracker = cv2.TrackerKCF_create()
# Wait a certain number of seconds to allow the camera time to warmup
sleep(0.1)
bbox1 = (640/2, 480/2, 50, 50)
# Capture frames continuously from the camera
p11 = (int(bbox1[0] - bbox1[2]), int(bbox1[1] - bbox1[3]))
p21 = (int(bbox1[0] + bbox1[2]), int(bbox1[1] + bbox1[3]))
key=[]
#ok = tracker.init(image, bbox1)
#key = cv2.waitKey(1) & 0xFF
for frame in camera.capture_continuous(raw_capture, format="bgr", use_video_port=True):
     
    # Grab the raw NumPy array representing the image
    image = frame.array
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #edged = cv2.Canny(gray, 35, 125)
    
    if key == ord('i'):
        ok = tracker.init(image, bbox1)
        print('reset')
    
    ok, bbox = tracker.update(image)
    #ok, bbox = tracker.update(image)
    
    if ok:
        # Tracking success
        p1 = (int(bbox[0] - bbox[2]), int(bbox[1] - bbox[3]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        image = cv2.rectangle(image, p1, p2, (255,0,0), 2, 1)
    else :
        # Tracking failure
        cv2.putText(image, "No Tracking", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
        cv2.rectangle(image, p11, p21, (255,0,0), 2, 1)
    # Display the frame using OpenCV

    cv2.imshow("Frame", image)
     
    # Wait for keyPress for 1 millisecond
    key = cv2.waitKey(1) & 0xFF
     
    # Clear the stream in preparation for the next frame
    raw_capture.truncate(0)
        
     
    # If the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
    # if i is pressed restart tracker
#    if key == ord('i'):
#        ok = tracker.init(image, bbox1)
#        ok, bbox = tracker.update(image)
#        print('restart')
#        print(ok)
#camera.start_preview()
#sleep(2)
#camera.capture('/home/pi/Desktop/test.jpg')
#camera.start_recording('/home/pi/Desktop/test.jpg')
#camera.start_recording('/home/pi/Desktop/video_test3.h264')
#sleep(10)
#camera.stop_recording()
#camera.stop_preview()
camera.close()
cv2.destroyAllWindows()