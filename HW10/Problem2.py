# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 19:10:04 2019

@author: Nate
"""

import numpy as np
import matplotlib.pyplot as plt
import pdb

##############################################################
##############################################################
#defining constants

#number of trials
N = int(1e4)


#α=0.2 to 2 in increments of 0.2

alpha = [1.6875]
rmax_list = [(2.1/alph) for alph in alpha]
r0 = np.array([2,2,2])
r1 = np.array([3,2,2])
energy = []
std_dev = []



#sigma = [4*i for i in alpha]
#rmax = 1/(2*alpha)



##############################################################
##############################################################
# NORMAL SAMPLES USING BOX-MUELLER METHOD
# DRAW SAMPLES FROM PROPOSAL DISTRIBUTION

for j in range(len(alpha)):
    u = np.array([])
    w = np.array([])
    u2 = np.array([])
    w2 = np.array([])
    u3 = np.array([])
    w3 = np.array([])
    
    for i in range(N):
        u = np.append(u ,np.random.uniform(0,1))
        w = np.append(w ,np.random.uniform(0,1))
        u2 = np.append(u2 ,np.random.uniform(0,1))
        w2 = np.append(w2 ,np.random.uniform(0,1))
        u3 = np.append(u3 ,np.random.uniform(0,1))
        w3 = np.append(w3 ,np.random.uniform(0,1))
    
    r = np.array([np.sqrt(-2*np.log(i)) for i in u])
    theta = np.array([2*np.pi*i for i in w])
    r2 = np.array([np.sqrt(-2*np.log(i)) for i in u2])
    theta2 = np.array([2*np.pi*i for i in w2])
    r3 = np.array([np.sqrt(-2*np.log(i)) for i in u3])
    theta3 = np.array([2*np.pi*i for i in w3])

    
    x = np.array([])
    y = np.array([])
    z = np.array([])
    x2 = np.array([])
    y2 = np.array([])
    z2 = np.array([])
    
    for i in range(N):
        x = np.append(x, np.array(r[i]*np.cos(theta[i])))
        y = np.append(y, np.array(r[i]*np.sin(theta[i])))
        z = np.append(z, np.array(r2[i]*np.cos(theta2[i])))
        x2 = np.append(x2, np.array(r2[i]*np.cos(theta2[i])))
        y2 = np.append(y2, np.array(r3[i]*np.sin(theta3[i])))
        z2 = np.append(z2, np.array(r3[i]*np.cos(theta3[i])))













###################################################################
###################################################################

print(r)
print(r2)

fig1, axes = plt.subplots(2, 3)
fig1.subplots_adjust(top=0.92, left=0.07, right=0.97, hspace=0.3, wspace=0.3)
((ax1, ax2, ax3), (ax4, ax5, ax6)) = axes  # unpack the axes

ax1.hist(theta,100)
ax1.set_ylabel('Counts')
ax1.set_xlabel('$theta_i$')
ax1.set_title("Theta", va='bottom')

ax2.hist(r,100)
ax2.set_ylabel('Counts')
ax2.set_xlabel('$R_i$')
ax2.set_title("R", va='bottom')

ax3.hist(r2,100)
ax3.set_ylabel('Counts')
ax3.set_xlabel('$R_i$')
ax3.set_title("R2", va='bottom')

ax4.hist(x,100)
ax4.set_ylabel('Counts')
ax4.set_xlabel('$x_i$')
ax4.set_title("X", va='bottom')

ax5.hist(y,100)
ax5.set_ylabel('Counts')
ax5.set_xlabel('$y_i$')
ax5.set_title("Y", va='bottom')

ax6.hist(z,100)
ax6.set_ylabel('Counts')
ax6.set_xlabel('$z_i$')
ax6.set_title("Z", va='bottom')





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

    print(rmax_list[i], 'accepted: ',count, 'rejected: ',N-count, '  Acceptance Ratio: ', count/N)
    energy.append(en/N)
    
    
    to_sum = 0
    for j in range(N):
        to_sum += (-(alpha[i]**2)/2 + alpha[i]/np.linalg.norm(r[j]) - 1/np.linalg.norm(r[j])-energy[i])**2
    
    std_dev.append(np.sqrt(to_sum)/np.sqrt(N))
    

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




