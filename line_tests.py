#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 22:04:38 2020

@author: pi
"""

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp


#Link lengths
AB = 1
BD = .5
CD = 1
DE = 2

#initial conditions
a_x = 0
a_y = 0


c_x = 1
c_y = 0

theta_a = 90
theta_b = 90

#create symboles
b_a, b_y, = sp.symbols('b_x b_y')

link_1_s= np.array([0,0])
link_1_f= np.array([0,2])
link_array= link_1_s,link_1_f

link_2_s= np.array([1,0])
link_2_f= np.array([1,2])


link_3_s = link_1_f
link_3_f = np.subtract(link_2_f , link_1_f)/np.linalg.norm(np.subtract(link_2_f , link_1_f))*4

plt.plot()