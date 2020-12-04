#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 21:21:19 2020

@author: pi
"""

from imutils import paths
import numpy as np
import imutils
import cv2
import os
os.chdir(r'/home/pi/Desktop')
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
    cnts = imutils.grab_contours(cnts)
    c = max(cnts, key = cv2.contourArea)
    # compute the bounding box of the of the paper region and return it
    return cv2.minAreaRect(c)


image=cv2.imread('test2.jpg')
#temp = find_marker(image)
cv2.startWindowThread()
cv2.namedWindow('test')
cv2.imshow('test', image)
cv2.waitKey(1)
#cv2.destroyAllWindows()
