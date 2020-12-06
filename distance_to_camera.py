#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 21:21:19 2020

@author: pi
"""

#from imutils import paths
import numpy as np
#import imutils
import cv2
import os
#os.chdir(r'/home/pi/Desktop')
def find_marker(image):
    # convert the image to grayscale, blur it, and detect edges
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(gray, 35, 125)
    print(edged)
    cv2.imshow('edged',edged)
    # find the contours in the edged image and keep the largest one;
    # we'll assume that this is our piece of paper in the image
    cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    #cnts = imutils.grab_contours(cnts)
    c = max(cnts, key = cv2.contourArea)
    # compute the bounding box of the of the paper region and return it
    return cv2.minAreaRect(c)


image=cv2.imread('test2.jpg')
#temp = find_marker(image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(gray, 35, 125)
cv2.startWindowThread()
cv2.namedWindow('test')
cv2.imshow('test', edged)
cv2.waitKey(0)
cv2.destroyAllWindows()

video = cv2.VideoCapture('IMG_4208.mp4')
ok, frame = video.read()

ok, frame1 = video.read()
#tracker = cv2.TrackerKCF_create()
tracker = cv2.TrackerMIL_create()
#tracker = cv2.TrackerBoosting_create()
#tracker = cv2.TrackerMOSSE_create()

#bbox = (100, 200, 200, 500)
#bbox = (160, 290, 100, 100)
bbox = (330, 100, 100, 100)
ok = tracker.init(frame, bbox)

while True:
        # Read a new frame
    ok, frame = video.read()
    if not ok:
        cv2.destroyAllWindows()
        break

    # Start timer
    timer = cv2.getTickCount()

    # Update tracker
    ok, bbox = tracker.update(frame)

    # Calculate Frames per second (FPS)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);

    # Draw bounding box
    if ok:
        # Tracking success
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
    else :
        # Tracking failure
        cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)

    # Display tracker type on frame
    cv2.putText(frame,  " Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);

    # Display FPS on frame
    cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);

    # Display result
    cv2.imshow("Tracking", frame)

    # Exit if ESC pressed
    k = cv2.waitKey(1) & 0xff
    if k == 27 : break

cv2.imshow('test', frame1)



bbox = (100, 250, 100, 100)
p1 = (int(bbox[0]), int(bbox[1]))
p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
cv2.rectangle(frame1, p1, p2, (255,0,0), 2, 1)
cv2.waitKey(0)
cv2.destroyAllWindows()