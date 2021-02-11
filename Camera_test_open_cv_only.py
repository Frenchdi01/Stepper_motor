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
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
ControlPin = [7,11,13,15]

for pin in ControlPin:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin, False)
    
seq=[ [1,0,0,0],
      [1,1,0,0],
      [0,1,0,0],
      [0,1,1,0],
      [0,0,1,0],
      [0,0,1,1],
      [0,0,0,1],
      [1,0,0,1],]
step_seq_num=0
camera = PiCamera()
camera.resolution = (720,720)
camera.framerate = 20

# Generates a 3D RGB array and stores it in rawCapture
raw_capture = PiRGBArray(camera, size=(720, 720))

#tracker = cv2.TrackerMIL_create()
#tracker = cv2.TrackerKCF_create()
tracker = cv2.TrackerCSRT_create()
#tracker = cv2.TrackerBoosting_create()
#tracker = cv2.TrackerMOSSE_create()

# Wait a certain number of seconds to allow the camera time to warmup
sleep(0.1)
bbox1 = (720/2, 720/2, 100, 100)
# Capture frames continuously from the camera
p11 = (int(bbox1[0] - bbox1[2]), int(bbox1[1] - bbox1[3]))
p21 = (int(bbox1[0] + bbox1[2]), int(bbox1[1] + bbox1[3]))

#ok = tracker.init(image, bbox1)
#key = cv2.waitKey(1) & 0xFF
for frame in camera.capture_continuous(raw_capture, format="bgr", use_video_port=True):
     
    # Grab the raw NumPy array representing the image
    image = frame.array
#    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#    image = cv2.Canny(image, 35, 125)
    
    #ok, bbox = tracker.update(image)
    # if i is pressed restart tracker
    
    ok, bbox = tracker.update(image)
    if ok:
        # Tracking success
        p1 = (int(bbox[0] - bbox[2]), int(bbox[1] - bbox[3]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(image, p1, p2, (255,0,0), 2, 1)
        print(bbox[0])
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
    if key == ord('i'):
        tracker = cv2.TrackerCSRT_create()
        ok = tracker.init(image, bbox1)
        cv2.rectangle(image, p11, p21, (255,0,0), 2, 1)
        print('restart')
        print(ok)    
    rotation = .1
    number_of_steps = int(rotation*4096)
    if bbox[0]>500:
        
        rotate_dir=1
        for i in range(0,number_of_steps+1):
            for pin in range(0,4):
                #print(pin)
                Pattern_Pin = ControlPin[pin]
                #print(Pattern_Pin)
                #print(seq[step_seq_num][pin])
                if seq[step_seq_num][pin] == 1:
                    GPIO.output(Pattern_Pin,True)
                    #print(Pattern_Pin)
                else: 
                    GPIO.output(Pattern_Pin,False)
                #print(seq[step_seq_num])    
            step_seq_num = step_seq_num + rotate_dir
            
            if(step_seq_num >=8):
                step_seq_num = 0
            elif step_seq_num<0:
                step_seq_num=7
            time.sleep(.001)
        else :
            rotate_dir=0
    
    
           

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
GPIO.cleanup()