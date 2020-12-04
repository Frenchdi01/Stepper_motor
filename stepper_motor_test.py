# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

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
#number_of_rot = float(input('Imput number of rotations : '))
rotate_dir=1
step_seq_num=0

step_sequence = [.25, .5, .75, 1, 1.25, 1.5, 1.75, 2,10]
for rotation in step_sequence:
    number_of_steps = int(rotation*4096)
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
        if number_of_steps/2==i:
            #rotate_dir=rotate_dir*-1
            time.sleep(.5)
        time.sleep(.001)
    time.sleep(.5)
GPIO.cleanup()