# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 15:11:54 2019

@author: Nate
"""

import numpy as np
import matplotlib.pyplot as plt

N1 = int(1e4)
x10, x20 = 1.1, 2.2

tau = np.arange(1, 10.1, .5)
r_max = 2


def G2(x1, x2, dt):
    return np.exp(-(x1-x2)**2/(2*dt)-dt/4*(x1*x1+x2*x2)) / np.sqrt(2*np.pi*dt)

def P1(x1, x2, dt):
    return dt*np.sqrt(4+dt*dt) * G2(x1,x2,dt) * G2(x2,x1,dt)

def Metropolis2P(DT, X10, X20, P, NITER, RMAX = r_max):
    X1 = np.append(X10, np.zeros(NITER))
    X2 = np.append(X20, np.zeros(NITER))
    NACC = 0
    
    for n in range(NITER):
        dR = RMAX*(np.random.rand(2)-.5)
        ratio = P(X1[n]+dR[0], X2[n]+dR[1], DT)/P(X1[n], X2[n], DT)
        ran = np.random.rand()
        if ratio>1 or ratio>ran:
            X1[n+1] = X1[n]+dR[0]
            X2[n+1] = X2[n]+dR[1]
            NACC += 1
        else:
            X1[n+1] = X1[n]
            X2[n+1] = X2[n]
    
    print(str(NACC/NITER*100)+'% accepted')
    
    return np.array([X1, X2])

EL1_dat = np.zeros((len(tau), N1+1))


def Summand1(X1, X2, DT):
    return (-(X1*X1+X2*X2)*(DT**4+8) + (4*DT+8*X1*X2)*(2+DT*DT)) / (16*DT*DT)

for i in range(len(tau)):
    x1,x2 = Metropolis2P(tau[i]/2, x10, x20, P1, N1)
    EL1_dat[i] = Summand1(x1, x2, tau[i]/2)
    
EL1_arr = np.average(EL1_dat, axis=1)
err1 = np.average(EL1_dat, axis=1)/np.sqrt(N1)

tau1_x = np.linspace(1,10,100)
El1_anal = 1/2 + np.exp(-tau1_x)/(1 - np.exp(-tau1_x))

plt.figure()
plt.plot(tau1_x, El1_anal, 'y', label='Analytical')
plt.plot(tau, EL1_arr, label='Monte-Carlo')
plt.xlabel(r'$\tau$')
plt.ylabel(r'$\langle E_L\rangle (\tau)$')
plt.show()
