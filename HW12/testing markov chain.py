# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 13:16:02 2019

@author: Nate
"""

import random

#number of runs
n = 100000

x0 = random.uniform(0, 1)
tracker = [0,0,0]


if x0 <= .5:
    x0 = 'x1'
elif x0 > .5 and x0 <= .7:
    x0 = 'x2'
else:
    x0 = 'x3'



for i in range(n):
    test = random.uniform(0, 1)
    
    
    if x0 == 'x1':
        x0 = 'x2' 
    elif x0 == 'x2':
        if test >= .1:
            x0 = 'x3'
    else:
        if test <= .6:
            x0 = 'x1'
        else:
            x0 = 'x2'
        
    
    if x0 == 'x1':
        tracker[0] += 1
    elif x0 == 'x2':
        tracker[1] += 1
    else:
        tracker[2] += 1
        
print(tracker, tracker[0]/n, tracker[1]/n, tracker[2]/n, sum(tracker)/n)