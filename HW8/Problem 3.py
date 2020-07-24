# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 19:46:14 2019

@author: Nate
"""

import numpy as np
import matplotlib.pyplot as plt
import pdb


'''
Determine the value of π to ≈ 14 digits by solving for the root of the equation

f(x) = cos(x) = 0

using the second order Newton’s method. The exact solution is 

    x∗ = π/2, so that π = 2x∗.

Use the initial guess of x = 1.5, corresponds to a guess of π ≈ 3. How many
iterations are needed to achieve 14 digits? Repeat the calculation with initial guesses
x = 1, x = 0.5 and x = 0.25.
'''

def f(guess):
    return(np.cos(guess))

def df(guess):
    return(-np.sin(guess))



guess = [1.5,1,.5,.25]


for i in range(len(guess)):
    for val in range(4):
        nextguess = guess[i] - f(guess[i])/df(guess[i])
        guess[i] = nextguess
        
    if i == 3:
        answer = guess[i]
        #print(guess[i])
        #print(answer)
        print(i, ": " , (3/2)*np.pi-answer)
        if abs((3/2)*np.pi-answer) < 10**(-12):
            print('True')
    else:
        answer = 2*guess[i]
        print(i, ": " , np.pi-answer)
        if abs(np.pi-answer) < 10**(-12):
            print('True')
            
print(10**(-10))