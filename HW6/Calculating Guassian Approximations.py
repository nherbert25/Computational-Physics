# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 17:38:46 2019

@author: Nate
"""
import math


x = (1+(.5-1/(2*math.sqrt(3)))**2)

y = (1+(.5+1/(2*math.sqrt(3)))**2)

#print(2*(1/x+1/y))


x = (1+(.5-1/(2*math.sqrt(3)))**2)

y = (1+(.5+1/(2*math.sqrt(3)))**2)

#print(2*(1/x+1/y))







'''
#2 point constants
x1 = 1/math.sqrt(3)
x2 = -1/math.sqrt(3)
c1 = 1
c2 = 1

c3 = 0
x3 = 1
'''

def funct(x):
    return(4/(1+x**2))
    
    
#print('3-Point Simpson for half integral function: ',(1/12)*(funct(0)+4*funct(.25)+2*funct(.5)+4*funct(.75)+funct(1)))

   
def threepoint(a,b):
    cont = (b-a)/2
    cont2 = (b+a)/2
    #3 point constants
    x1 = math.sqrt(15)/5
    x2 = -math.sqrt(15)/5
    c1 = 5/9
    c2 = 5/9
    c3 = 8/9    
    x3 = 0.0

    to_return = cont*(c1*funct(cont*x1+cont2)+c2*funct(cont*x2+cont2)+c3*funct(cont*x3+cont2))
    return(to_return)


def twopoint(a,b):
    cont = (b-a)/2
    cont2 = (b+a)/2
    #2 point constants
    x1 = 1/math.sqrt(3)
    x2 = -1/math.sqrt(3)
    c1 = 1
    c2 = 1
    to_return = cont*(c1*funct(cont*x1+cont2)+c2*funct(cont*x2+cont2))
    return(to_return)





print('output of function: ',threepoint(0,.5)+threepoint(.5,1))
