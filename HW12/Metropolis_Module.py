# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 09:51:21 2019

@author: Nate
"""

import numpy as np
import pdb

##############################################################
##############################################################
#defining functions


def get_delta_r(rmax):
    delta_r = np.array([rmax*(np.random.uniform()-.5),rmax*(np.random.uniform()-.5),rmax*(np.random.uniform()-.5)])
    return(delta_r)

#evaluate ratio
def evaluate_ratio(r, delta_r,r2, delta_r2, alpha):
    global count
    A = np.exp(-2*alpha*np.linalg.norm(r))*np.exp(-2*alpha*np.linalg.norm(r2))
    B = np.exp(-2*alpha*np.linalg.norm(r+delta_r))*np.exp(-2*alpha*np.linalg.norm(r2+delta_r2))
    ratio = B/A
    
    
    if ratio > np.random.uniform():
        #count+=1
        return(True)
    else:
        return(False)

def generate_point(r, delta_r, r2, delta_r2, alpha):
    if evaluate_ratio(r, delta_r, r2, delta_r2, alpha) == True:
        return(r+delta_r, r2+delta_r2)
    else:
        return(r, r2)


##############################################################
##############################################################

#take in r1, r2
#generate new point
#evaluate if point moves
#return r1, r2


def metropolis(r1, r2, alpha):
    #generating points
    r = np.array(r1)
    r2 = np.array(r2)
    #en = 0
    
    #r2=np.random.exponential(.5/alpha[i])
    #en +=-alpha[i]**2 + alpha[i]/np.linalg.norm(r2) - 1/np.linalg.norm(r2)

    x , y = generate_point(r, get_delta_r((2.1/alpha)), r2, get_delta_r((2.1/alpha)), alpha)
    x , y = list(x), list(y)


    #pdb.set_trace()
    #pdb.set_trace()
    #r = np.append(r, [x], axis = 0)
    #r2 = np.append(r2, [y], axis = 0)
    
    #pdb.set_trace()
    '''
    r_mag = np.linalg.norm([r[j][0], r[j][1], r[j][2]])
    r2_mag = np.linalg.norm([r2[j][0], r2[j][1], r2[j][2]])
    r12 = np.sqrt((r[j][0]-r2[j][0])**2 + (r[j][1]-r2[j][1])**2 + (r[j][2]-r2[j][2])**2)+.0000001
    
    
    E1 = -(1/2.0)*alpha**2+ alpha/r_mag-2/r_mag
    E2 = -(1/2.0)*alpha**2+ alpha/r2_mag-2/r2_mag
    en += E1 + E2 + (1.0/r12)
    ''' 
    
    return list([list(x), list(y)])
    
##############################################################################
##############################################################################
