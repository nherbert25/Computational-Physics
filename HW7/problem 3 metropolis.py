# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:48:44 2019

@author: Nate
"""

import numpy as np
import matplotlib.pyplot as plt
import pdb

#fig2, axes2 = plt.subplots()


##############################################################
##############################################################
#defining constants

#number of trials
N = 10000


#α=0.2 to 2 in increments of 0.2

alpha = [i*.2 for i in range(1,11)]
rmax_list = [(2.1/alph) for alph in alpha]
r0 = np.array([2,2,2])
r1 = np.array([3,2,2])
energy = []
std_dev = []



#sigma = [4*i for i in alpha]
#rmax = 1/(2*alpha)




##############################################################
##############################################################
#defining functions


def get_delta_r(rmax):
    delta_r = np.array([rmax*(np.random.uniform()-.5),rmax*(np.random.uniform()-.5),rmax*(np.random.uniform()-.5)])
    return(delta_r)

#evaluate ratio
def evaluate_ratio(r, delta_r,r2, delta_r2):
    global count
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



for i in range(len(alpha)):

    #generating points
    r = np.array([r0])
    r2 = np.array([r1])
    count = 0
    en = 0
    
    for j in range(N):
        #r2=np.random.exponential(.5/alpha[i])
        #en +=-alpha[i]**2 + alpha[i]/np.linalg.norm(r2) - 1/np.linalg.norm(r2)

        x , y = generate_point(r[len(r)-1], get_delta_r(rmax_list[i]), r2[len(r2)-1], get_delta_r(rmax_list[i]))

        #pdb.set_trace()
        r = np.append(r, [x], axis = 0)
        r2 = np.append(r2, [y], axis = 0)
        
        #pdb.set_trace()
        r_mag = np.linalg.norm([r[j][0], r[j][1], r[j][2]])
        r2_mag = np.linalg.norm([r2[j][0], r2[j][1], r2[j][2]])
        r12 = np.sqrt((r[j][0]-r2[j][0])**2 + (r[j][1]-r2[j][1])**2 + (r[j][2]-r2[j][2])**2)+.0000001
        
        
        E1 = -(1/2.0)*alpha[i]**2+ alpha[i]/r_mag-2/r_mag
        E2 = -(1/2.0)*alpha[i]**2+ alpha[i]/r2_mag-2/r2_mag
        en += E1 + E2 + (1.0/r12)
        
        
##############################################################################
##############################################################################
        


    print(rmax_list[i], 'accepted: ',count, 'rejected: ',N-count)
    print('Acceptance Ratio: ', count/N)
    energy.append(en/N)
    
    
    to_sum = 0
    for j in range(N):
        to_sum += (-(alpha[i]**2)/2 + alpha[i]/np.linalg.norm(r[j]) - 1/np.linalg.norm(r[j])-energy[i])**2
    
    std_dev.append(np.sqrt(to_sum)/np.sqrt(N))
    
    '''
    if i == 1:
        axes2.hist([np.linalg.norm(i) for i in r], bins = 100, normed = True)
        axes2.plot([n*.1 for n in range(0,3000)]    , [2*alpha[i]*np.e**(-2*alpha[i]*n*.1)  for n in range(0,3000)])
'''


print(energy)

##############################################################
##############################################################
#Plotting


std_dev = [sev/20 for sev in std_dev]

fig1, axes1 = plt.subplots()

#axes1.scatter(alpha, [3/2*num-2**(3/2)/(np.pi**.5)*num**.5 for num in alpha])
#axes1.scatter(8/(9*np.pi), 3/2*(8/(9*np.pi))-2**(3/2)/(np.pi**.5)*(8/(9*np.pi))**.5)
#axes1.plot(alpha, energy)
axes1.errorbar(alpha, energy, yerr=std_dev, fmt='o', linestyle = '-')
axes1.plot(alpha, [num**2- 27*num/8 for num in alpha])

axes1.set_ylabel('Energy')
axes1.set_xlabel('alpha')
axes1.set_title("Energy vs alpha", va='bottom')


plt.show()