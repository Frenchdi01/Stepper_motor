#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 22:00:42 2020

@author: pi
"""

import numpy as np
import sympy as sp
import pandas as pd
import matplotlib.pyplot as plt

#links
AB=.5
CD=1
BC=.3
CE=2

#initial conditions
a_x= 0
a_y= 0

d_x=-5
d_y=2

theta_a = 90

theta_a=range(0,300,180)
list_ax = []
list_ay = []
list_bx = []
list_by = []
list_cx = []
list_cy = []
list_dx = []
list_dy = []
list_ex = []
list_ey = []
for i in theta_a:
    b_xs, b_ys =  sp.symbols('b_xs b_ys')
    
    c_xs, c_ys = sp.symbols('c_xs c_ys')
    
    e_xs, e_ys = sp.symbols('e_xs e_ys')
    
    
    b_x = AB*np.cos(np.radians(i))
    b_y = AB*np.sin(np.radians(i))
    
    #location of D
    equ1 = sp.Eq(  (c_xs - b_x)**2 + (c_ys - b_y)**2 - BC**2 , 0 )
    equ2 = sp.Eq(  (c_xs - d_x)**2 + (c_ys - d_y)**2 - CD**2 , 0 )
    
    try: 
        C=sp.solve((equ1, equ2), (c_xs, c_ys))
        
        C_0=C[0]
        C_1=C[1]
        
        #if b_x<C_0[0]:
        if C_0[1]>.5 and C_0[0]>0:
            c_x=C_0[0]
            c_y=C_0[1]
        else:
            c_x=C_1[0]
            c_y=C_1[1]
    except TypeError:
        c_x=np.nan
        c_y=np.nan
    
    
    unit_BD_x = (c_x - b_x)/BC
    unit_BD_y = (c_y - b_y)/BC
    
    
    e_x = c_x + unit_BD_x*CE
    e_y = c_y + unit_BD_y*CE
    
    list_ax.append(a_x)
    list_ay.append(a_y)
    list_bx.append(b_x)
    list_by.append(b_y)
    list_cx.append(c_x)
    list_cy.append(c_y)
    list_dx.append(d_x)
    list_dy.append(d_y)
    list_ex.append(e_x)
    list_ey.append(e_y)

#%% 
df = pd.DataFrame({ \
       'theta':theta_a,\
        'a_x' :list_ax,\
        'a_y' :list_ay,\
        'b_x' :list_bx,\
        'b_y' :list_by,\
        'c_x' :list_cx,\
        'c_y' :list_cy,\
        'd_x' :list_dx,\
        'd_y' :list_dy,\
        'e_x' :list_ex,\
        'e_y' :list_ey,\
        })
    
plot_ab = lambda row: plt.plot([row['a_x'],row['b_x']],[row['a_y'],row['b_y']], 'b-', alpha=.3 )
plot_bc = lambda row: plt.plot([row['b_x'],row['c_x']],[row['b_y'],row['c_y']], 'k-', alpha=.3 )
plot_cd = lambda row: plt.plot([row['d_x'],row['c_x']],[row['d_y'],row['c_y']], 'r-', alpha=.3 )
plot_ce = lambda row: plt.plot([row['c_x'],row['e_x']],[row['c_y'],row['e_y']], 'g-', alpha=.3 )
plot_point_e = lambda row: plt.plot(row['e_x'],row['e_y'],'+g')
plt.figure()
df.apply(plot_ab,axis=1)
df.apply(plot_bc,axis=1)
df.apply(plot_cd,axis=1)
df.apply(plot_ce,axis=1)
df.apply(plot_point_e, axis=1)
plt.grid(True)
plt.title('AB= ' + str(AB) + ', CD= ' + str(CD) + ', BC= ' + str(BC) + ', CE= ' + str(CE) + '\n' \
          + '(a_x, a_y)= (' + str(a_x) + ',' + str(a_y) + ') ' + '(d_x, d_y)= (' + str(d_x) +','+ str(d_y) +')')
plt.show()