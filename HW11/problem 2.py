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

#number of trials
N = int(3e4)


alpha = 1.6875
time_step = [0.09,0.08,0.07,0.06,0.05,0.04,0.03,0.02,0.01]
r0 = np.array([2,2,2])
r1 = np.array([3,2,2])
energy = []
std_dev = []



##############################################################
##############################################################
#defining functions


def get_delta_r(rmax):
    delta_r = np.array([rmax*(np.random.uniform()-.5),rmax*(np.random.uniform()-.5),rmax*(np.random.uniform()-.5)])
    return(delta_r)

#evaluate ratio
def evaluate_ratio(r, delta_r,r2, delta_r2):
    global count
    #(P = B/A)
    A = np.exp(-2*alpha[i]*np.linalg.norm(r))*np.exp(-2*alpha[i]*np.linalg.norm(r2))
    B = np.exp(-2*alpha[i]*np.linalg.norm(r+delta_r))*np.exp(-2*alpha[i]*np.linalg.norm(r2+delta_r2))
    ratio = B/A
    
    if ratio > np.random.uniform():
        count+=1
        return(True)
    else:
        return(False)

def generate_point(r, delta_r, r2, delta_r2):
    if evaluate_ratio(r, delta_r, r2, delta_r2) == True:
        return(r+delta_r, r2+delta_r2)
    else:
        return(r, r2)


##############################################################
##############################################################
#Main Loop

for i in range(len(time_step)):

    #generating points
    r = np.array([r0])
    r2 = np.array([r1])
    count = 0
    en = 0
    
    for j in range(N):

        #evaluate v_x1, v_y1 etc
        current_r = r[-1]
        current_r2 = r2[-1]
        r_normal = np.array([np.random.randn(),np.random.randn(),np.random.randn()])
        r2_normal = np.array([np.random.randn(),np.random.randn(),np.random.randn()])
        
        
        r_to_add = current_r - alpha*current_r/np.linalg.norm(current_r) + np.sqrt(time_step[i])*r_normal
        r2_to_add = current_r2 - alpha*current_r2/np.linalg.norm(current_r2) + np.sqrt(time_step[i])*r2_normal


        #record energy
        r = np.append(r, [r_to_add], axis = 0)
        r2 = np.append(r2, [r2_to_add], axis = 0)
        
        r_mag = np.linalg.norm([r[j][0], r[j][1], r[j][2]])
        r2_mag = np.linalg.norm([r2[j][0], r2[j][1], r2[j][2]])
        r12 = np.sqrt((r[j][0]-r2[j][0])**2 + (r[j][1]-r2[j][1])**2 + (r[j][2]-r2[j][2])**2)+.0000001
        
        
        E1 = -(1/2.0)*alpha**2+ alpha/r_mag-2/r_mag
        E2 = -(1/2.0)*alpha**2+ alpha/r2_mag-2/r2_mag
        en += E1 + E2 + (1.0/r12)
        

    #print('accepted: ',count, 'rejected: ',N-count)
    #print('Acceptance Ratio: ', count/N)
    energy.append(en/N)
    print('Finished run: ', time_step[i])
    
    '''
    to_sum = 0
    for j in range(N):
        to_sum += (-(alpha[i]**2)/2 + alpha[i]/np.linalg.norm(r[j]) - 1/np.linalg.norm(r[j])-energy[i])**2
    
    std_dev.append(np.sqrt(to_sum)/np.sqrt(N))
    '''
print(energy)




##############################################################
##############################################################
#Plotting


fig1, axes1 = plt.subplots()
axes1.plot(time_step, energy)
axes1.plot(np.linspace(0, .09, num=50), [-2.845 for i in range(50)])
axes1.set_ylabel('Energy')
axes1.set_xlabel('Time Step Sizes $\Delta t$')
axes1.set_title("Energy vs $\Delta t$", va='bottom')


plt.show()




