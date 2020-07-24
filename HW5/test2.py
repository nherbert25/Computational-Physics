# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 16:54:45 2019

@author: Nate
"""

import numpy as np
import useful as use


sx = 10 #size of box
sy = 10
sz = 10

dt = .01 #timestep
t_total = 10

x = np.array([7,3], dtype=float)
y = np.array([6,6], dtype=float)
z = np.array([0,0], dtype=float)
vx = np.array([0,.4], dtype=float)
vy = np.array([0,0], dtype=float)
vz = np.array([0,0], dtype=float)
ax = np.array([0,0], dtype=float)
ay = np.array([0,0], dtype=float)
az = np.array([0,0], dtype=float)
kinetic = []
potential = []
N = len(x)

pot = 0 #potential energy?


#print(x+y)

def test(N, x, y, z, sx, sy, sz):

    global ax,ay,az
    for i in range(N):
        ax[i] = 0
        ay[i] = 0
        az[i] = 0

    pot = 0
    
    
    print('da as ',ax,ay,az)
    for i in range(N-1):
        #print('thisisi',i)
        for j in range((i+1),N):
            #print(j)
            #print(i,j)
            dx = x[i] - x[j]
            dy = y[i] - y[j]
            dz = z[i] - z[j]
            ax[i] = 3.3
            print(ax)

test(N, x, y, z, sx, sy, sz)
