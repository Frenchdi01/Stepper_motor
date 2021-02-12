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
AB = 6*4
DC = 6*4
BC = .707*4
CE = 6*4
HI = 6*4
IC = 1*4
DH = 1*4
CG = BC

#initial conditions
a_x = -.5*4
a_y = .5*4

d_x = 0
d_y = 0


theta_d = 90
theta_h = [130]

h_x = DH*np.cos(np.radians(theta_h))
h_y = DH*np.sin(np.radians(theta_h))
#pivot_triangle= np.sqrt(.707**2-(.707/2)**2)
pivot_triangle =  BC*np.sin(np.radians(60))

theta_d=range(30,160,10)
theta_h=range(150,191,10)
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

list_fx = []
list_fy = []
list_gx = []
list_gy = []
list_hx = []
list_hy = []
list_ix = []
list_iy = []

list_theta_h=[]
list_theta_d=[]
for x in theta_h:
    h_x = d_x + DH*np.cos(np.radians(x))
    h_y = d_y + DH*np.sin(np.radians(x))
    for i in theta_d:
        b_xs, b_ys =  sp.symbols('b_xs b_ys')
        
        c_xs, c_ys = sp.symbols('c_xs c_ys')
        
        e_xs, e_ys = sp.symbols('e_xs e_ys')
        
        i_xs, i_ys = sp.symbols('i_xs i_ys')
        
        
        c_x = d_x + DC*np.cos(np.radians(i))
        c_y = d_y + DC*np.sin(np.radians(i))
        
        #location of D
        equ1 = sp.Eq(  (b_xs - c_x)**2 + (b_ys - c_y)**2 - BC**2 , 0 )
        equ2 = sp.Eq(  (b_xs - a_x)**2 + (b_ys - a_y)**2 - AB**2 , 0 )
        
        try: 
            B=sp.solve((equ1, equ2), (b_xs, b_ys))
            
            B_0=B[0]
            B_1=B[1]
            
            #if b_x<C_0[0]:
            #if B_0[1]>-1 and B_0[0]>0:
            if B_0[1]>0:
                b_x=B_0[0]
                b_y=B_0[1]
            else:
                b_x=B_1[0]
                b_y=B_1[1]
        except (TypeError, IndexError):
            b_x=np.nan
            b_y=np.nan
        
        
        unit_BC_x = (c_x - b_x)/BC
        unit_BC_y = (c_y - b_y)/BC
        
        perp_unitBC_x = -unit_BC_y
        perp_unitBC_y = unit_BC_x
        
        g_x = b_x + unit_BC_x*BC/2 + perp_unitBC_x*pivot_triangle
        g_y = b_y + unit_BC_y*BC/2 + perp_unitBC_y*pivot_triangle
        
        equ1 = sp.Eq(  (i_xs - c_x)**2 + (i_ys - c_y)**2 - IC**2 , 0 )
        equ2 = sp.Eq(  (i_xs - h_x)**2 + (i_ys - h_y)**2 - HI**2 , 0 )
        
        try: 
            I=sp.solve((equ1, equ2), (i_xs, i_ys))
            
            I_0=I[0]
            I_1=I[1]
            
            #if b_x<C_0[0]:
            #if B_0[1]>-1 and B_0[0]>0:
            if I_0[1]>0:
                i_x=I_0[0]
                i_y=I_0[1]
            else:
                i_x=I_1[0]
                i_y=I_1[1]
        except (TypeError, IndexError):
            i_x=np.nan
            i_y=np.nan
            
        unit_IC_x = (c_x - i_x)/IC
        unit_IC_y = (c_y - i_y)/IC
        
        e_x = c_x + unit_IC_x*CE
        e_y = c_y + unit_IC_y*CE
        
        unit_CG_x = (g_x - c_x)/CG
        unit_CG_y = (g_y - c_y)/CG
        
        f_x = e_x + unit_CG_x*CG
        f_y = e_y + unit_CG_y*CG
        
        list_ax.append(a_x)
        list_ay.append(a_y)
        list_bx.append(b_x)
        list_by.append(b_y)
        list_cx.append(c_x)
        list_cy.append(c_y)
        list_dx.append(d_x)
        list_dy.append(d_y)
        list_gx.append(g_x)
        list_gy.append(g_y)
        
        list_ex.append(e_x)
        list_ey.append(e_y)
        list_hx.append(h_x)
        list_hy.append(h_y)
        list_ix.append(i_x)
        list_iy.append(i_y)
        list_fx.append(f_x)
        list_fy.append(f_y)
        list_theta_d.append(i)
        list_theta_h.append(x)
#%% 
df = pd.DataFrame({ \
        'theta_h': list_theta_h,\
        'theta':list_theta_d,\
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
        'f_x' :list_fx,\
        'f_y' :list_fy,\
        'g_x' :list_gx,\
        'g_y' :list_gy,\
        'h_x' :list_hx,\
        'h_y' :list_hy,\
        'i_x' :list_ix,\
        'i_y' :list_iy,\
        })
df = df.dropna()    
plot_ab = lambda row: plt.plot([row['a_x'],row['b_x']],[row['a_y'],row['b_y']], 'g-', alpha=.3 )
plot_bc = lambda row: plt.plot([row['b_x'],row['c_x']],[row['b_y'],row['c_y']], 'g-', alpha=.3 )
plot_cd = lambda row: plt.plot([row['d_x'],row['c_x']],[row['d_y'],row['c_y']], 'r-', alpha=.3 )
plot_ce = lambda row: plt.plot([row['c_x'],row['e_x']],[row['c_y'],row['e_y']], 'k-', alpha=.3 )
plot_bg = lambda row: plt.plot([row['b_x'],row['g_x']],[row['b_y'],row['g_y']], 'g-', alpha=.3 )
plot_cg = lambda row: plt.plot([row['c_x'],row['g_x']],[row['c_y'],row['g_y']], 'g-', alpha=.3 )
plot_hi = lambda row: plt.plot([row['h_x'],row['i_x']],[row['h_y'],row['i_y']], 'k-', alpha=.3 )
plot_ic = lambda row: plt.plot([row['i_x'],row['c_x']],[row['i_y'],row['c_y']], 'k-', alpha=.3 )
plot_dh = lambda row: plt.plot([row['d_x'],row['h_x']],[row['d_y'],row['h_y']], 'r-', alpha=.3 )
plot_ef = lambda row: plt.plot([row['e_x'],row['f_x']],[row['e_y'],row['f_y']], 'k-', alpha=.3 )
plot_gf = lambda row: plt.plot([row['g_x'],row['f_x']],[row['g_y'],row['f_y']], 'k-', alpha=.3 )
#plot_point_e = lambda row: plt.plot(row['e_x'],row['e_y'],'+g')
plt.figure()
df.apply(plot_ab,axis=1)
df.apply(plot_bc,axis=1)
df.apply(plot_cd,axis=1)
df.apply(plot_bg,axis=1)
df.apply(plot_cg,axis=1)
df.apply(plot_hi,axis=1)
df.apply(plot_ic,axis=1)
df.apply(plot_ce,axis=1)
df.apply(plot_dh,axis=1)
df.apply(plot_ef,axis=1)
df.apply(plot_gf,axis=1)
#df.apply(plot_point_e, axis=1)
plt.grid(True)
plt.title('AB= ' + str(AB) + ', DC= ' + str(DC) + ', BC= ' + str(BC) + ', CE= ' + str(CE) + '\n' \
          + '(a_x, a_y)= (' + str(a_x) + ',' + str(a_y) + ') ' + '(d_x, d_y)= (' + str(d_x) +','+ str(d_y) +')')

plt.show()