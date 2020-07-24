# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 16:49:26 2019

@author: Nate


Solve the time-dependent Schrodinger equation using the second-order FFT method as described in the lecture note. 

a. Examine the given program and see how the kinetic and potential arrays are ﬁrst, computed only once. 
    Run the program and see that at dt=0.05, the transmission coeﬃcient is 0.518982 as compared to the exact result of 0.52001. 

b. Out put |ψ(x)|2 at t=10, 15, 20, 25. 

c. Compute T(E) as a function of the initial energy for dt=0.05.
    Repeat the calculation using the fourth-order Forest-Ruth algorithm.
    Plot these two results against the exact Tex(E) as given in the lecture note.
    Plot also T(E)−Tex(E) for these two results in the same graph.
"""

import numpy as np
import matplotlib.pyplot as plt
import pdb

with open("test.txt") as file:

    #skips n rows, i.e, will plot t = n+1
    for i in range(0):
        file.readline()

    data = file.readline()
    
    #print(data[2])
    data = data.replace("  ", " ")
    data = data.split(" ")
    data = data[5:-1]
    for i in range(len(data)):
        data[i] = float(data[i])**2


fig1, axes1 = plt.subplots()
axes1.plot(np.linspace(0, 2**12, len(data)), data)

axes1.set_ylabel('$|\Psi^2(x)|$')
axes1.set_xlabel('x')
axes1.set_title("TDWF at t=1", va='bottom')


plt.show()
