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

T2_energy = []
T2_ratio = []
T2_exact = []
T2_difference = []

T4_energy = []
T4_ratio = []
T4_exact = []
T4_difference = []

with open("energy.txt") as file:
    
    
    for line in file:    
        data = line
        data = data.replace("  ", " ")
        data = data.replace("\n", "")
        data = data.split(" ")
        data = data[1:]
        data = [float(x) for x in data]
        
        T2_energy.append(data[0])
        T2_ratio.append(data[2]/data[1])
        T2_exact.append(data[3])
        T2_difference.append(data[2]/data[1]-data[3])

with open("energy4.txt") as file:
    for line in file:    
        data = line
        data = data.replace("  ", " ")
        data = data.replace("\n", "")
        data = data.split(" ")
        data = data[1:]
        data = [float(x) for x in data]
        
        T4_energy.append(data[0])
        T4_ratio.append(data[3])
        T4_exact.append(data[4])
        T4_difference.append(data[3]-data[4])
        





fig1, axes1 = plt.subplots()
axes1.plot(T2_energy, T2_difference, label = '2nd Order')
axes1.plot(T4_energy, T4_difference, label = 'Forest-Ruth')

axes1.set_ylabel('Ratio of Theory to Algorithm')
axes1.set_xlabel('Energy')
axes1.set_title("Ratio of Theory to Algorithm Vs. Energy", va='bottom')
axes1.legend()

fig2, axes2 = plt.subplots()
axes2.plot(T2_energy, T2_exact, label = 'Exact Solution')
axes2.plot(T2_energy, T2_ratio, label = 'T2 Solution')

axes2.set_ylabel('Transmitted Energy')
axes2.set_xlabel('Initial Energy')
axes2.set_title("T2 Algorithm: $T(E)$ vs $E_0$", va='bottom')
axes2.legend()


fig3, axes3 = plt.subplots()
axes3.plot(T4_energy, T4_exact, label = 'Exact Solution')
axes3.plot(T4_energy, T4_ratio, label = 'T4 Solution')

axes3.set_ylabel('Transmitted Energy')
axes3.set_xlabel('Initial Energy')
axes3.set_title("Forest Ruth: $T(E)$ vs $E_0$", va='bottom')
axes3.legend()
'''
fig4, axes4 = plt.subplots()
axes4.plot(T2_exact, T2_ratio, label = 'Exact Solution')

axes4.set_ylabel('Calcuated T(E)')
axes4.set_xlabel('Exact T(E)')
axes4.set_title("asdf", va='bottom')
axes4.legend()
'''

plt.show()