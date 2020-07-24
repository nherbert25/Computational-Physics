# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 16:16:12 2019

@author: Nate
"""

from scipy import random
import numpy as np
import matplotlib.pyplot as plt



a = 0
b = 1

N = 10000
xrand = random.uniform(a,b,N)

to_plot = []
to_plot_scatter = []

def my_func(x):
    return(4/(1+x**2))

plotting3 = []


integral = 0.0
for i in range(N):
    
    
    x = my_func(xrand[i])
    integral += my_func(xrand[i])
    answer = integral*(b-a)/(i+1)
    plotting3.append((answer-np.pi)/np.pi)
    
    to_plot.append(answer)
    to_plot_scatter.append(x)



fig1, ax3 = plt.subplots()
ax3.plot(to_plot)   
ax3.plot(range(N),np.full(N,np.pi),'r')
ax3.set_ylabel('Integral Evaluation')
ax3.set_xlabel('Counts')
ax3.set_ylim(1.9,4.1)
ax3.legend(('Approximate Integral','Exact'), loc='upper right')
ax3.set_title("Monte Carlo - $\int_{0}^{1} \\frac{4}{1+x^2} dx$", va='bottom')



fig1, ax4 = plt.subplots()

plotting2 = []
plotting2x = []
for i in range(N):
    plotting2.append(my_func(i/N))
    plotting2x.append(i/N)
    #plotting2.append(np.sin(i/N))
    
ax4.plot(plotting2x,plotting2)
ax4.set_ylabel('$f(x_i)$')
ax4.set_xlabel('$x_i$')
ax4.set_title("Exact Solution of $\\frac{4}{1+x^2}$", va='bottom')


fig1, ax5 = plt.subplots()
ax5.plot(np.zeros(N))
ax5.plot(plotting3)
ax5.set_ylabel('Error')
ax5.set_xlabel('Counts')
ax5.set_title("Accuracy", va='bottom')


fig1, ax6 = plt.subplots()
ax6.scatter(range(0,N),to_plot_scatter, s=.5)
ax6.set_ylabel('$f(x_i)$')
ax6.set_xlabel('Counts')
ax6.set_title("$f(x_i)$ at random points from 0 to 1", va='bottom')



plt.show()
