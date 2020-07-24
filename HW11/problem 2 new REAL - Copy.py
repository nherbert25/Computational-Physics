# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 17:38:08 2019

@author: Nate

The Generalized Metropolis algorithm removed the step-size error by an additional acceptance/rejection step, 
which adds substantial overhead. To improve on the ﬁrstorder Langevin algorithm, can you devise a second-order 
Langevin algorithm to reduce the step-size error dependence to (∆t)2?

Repeat problem 2 of HW10 using this second order Langevin algorithm.
"""

import numpy as np
import matplotlib.pyplot as plt
import pdb


##############################################################
##############################################################
#defining constants

N2 = 10000
alpha = 1.6875

g1 = np.random.randn(N2)
g2 = np.random.randn(N2)
g3 = np.random.randn(N2)
g4 = np.random.randn(N2)
g5 = np.random.randn(N2)
g6 = np.random.randn(N2)


gauss = np.array([[i,j,k,l,m,n] for i,j,k,l,m,n in zip(g1,g2,g3,g4,g5,g6)])
x0 = np.array([5,6,2,-2,-1,-8])
tau = np.append(np.arange(0.001,0.01,0.003), np.arange(0.01, 0.07, 0.01))
x = np.zeros((len(tau), N2, len(x0)))
EL2_dat = np.zeros((len(tau), N2))

##############################################################
##############################################################
#Function Definitions

def vel(x):
    r1 = np.sqrt(np.sum(x[:3]**2))
    r2 = np.sqrt(np.sum(x[3:]**2))
    v1 = -alpha*x[:3]/r1
    v2 = -alpha*x[3:]/r2
    return np.append(v1,v2)

def Langevin2(X0, VEL, GAUSS, DT, N):
    X = np.zeros((N,len(X0)))
    vel1 = VEL(X0)
    Y0 = X0 + VEL(X0+DT/4*vel1)*DT/2 + GAUSS[0]*np.sqrt(DT)
    vel2 = VEL(Y0)
    X[0] = Y0 + DT/2*VEL(Y0 + DT/4*vel2)
    
    for i in range(1,N):
        vel1 = VEL(X[i-1])
        Yi = X[i-1] + VEL(X[i-1] + DT/4*vel1)*DT/2 + GAUSS[i]*np.sqrt(DT)
        vel2 = VEL(Yi)
        X[i] = Yi + DT/2*VEL(Yi + DT/4*vel2)
        
    return X

def EL2(X1, Y1, Z1, X2, Y2, Z2, ALPHA = alpha):
    
    R1 = np.sqrt(X1**2 + Y1**2 + Z1**2)
    R2 = np.sqrt(X2**2 + Y2**2 + Z2**2)
    R12 = np.sqrt((X2-X1)**2 + (Y2-Y1)**2 + (Z2-Z1)**2)
    
    return ALPHA * (-ALPHA + 1/R1 + 1/R2) - 2/R1 - 2/R2 + 1/R12

##############################################################
##############################################################
#Main Loop

for i in range(len(tau)):
    
    x[i] = Langevin2(x0, vel, gauss, tau[i], N2)
    
    x1 = np.array([x[i,j,0] for j in range(N2)])
    y1 = np.array([x[i,j,1] for j in range(N2)])
    z1 = np.array([x[i,j,2] for j in range(N2)])
    x2 = np.array([x[i,j,3] for j in range(N2)])
    y2 = np.array([x[i,j,4] for j in range(N2)])
    z2 = np.array([x[i,j,5] for j in range(N2)])
    
    EL2_dat[i] = EL2(x1, y1, z1, x2, y2, z2)
    
EL2_arr = np.average(EL2_dat, axis=1)
err2 = np.std(EL2_dat, axis=1)/np.sqrt(N2/48**2)

##############################################################
##############################################################
#Plotting

fig1, axes1 = plt.subplots()
axes1.plot(tau, EL2_arr, 'o-', label = '2nd Order Langevin')
axes1.hlines(-729/256, 0, np.max(tau), linestyle='dashed', label = 'Theoretical')
axes1.set_ylabel('Energy')
axes1.set_xlabel('Time Step Sizes $\Delta t$')
axes1.set_title("Energy vs $\Delta t$", va='bottom')
axes1.legend()
plt.show()