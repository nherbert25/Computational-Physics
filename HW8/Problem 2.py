# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 14:16:41 2019

@author: Nate
"""

import numpy as np
import matplotlib.pyplot as plt
import pdb



delta_r = .01
l_orbital = [0,1,2,3]
#l_orbital = [0]
eps_list = []

#-1/r potential energies
#for i in range(1001):
#    eps_list.append(i*.001-1)


#r*r/2 potential energies
for i in range(1001):
    eps_list.append(i*.01)

#u(r-dt), u(r), l, r, eps
def stepping(u_2, u_1, l, r, eps):
    fun = 2*(r*r/2) + l*(l+1)/r**2 - 2*eps
    #fun = -2/r + l*(l+1)/r**2 - 2*eps
    u_3 = 2*u_1 - u_2 + delta_r**2*fun*u_1
    return(u_3)



##############################################################
##############################################################


good_points = []

for l in l_orbital:
    for eps in eps_list:
        u = [0, .01]
        r = delta_r*2
        
        
        for i in range(5000):
            u.append(stepping(u[-2],u[-1], l, r, eps))
            
            if u[-1]*u[-2] < 0:
                good_points.append([l, eps, r])
                
            r+=delta_r
            u = [u[-2],u[-1]]
            

##############################################################
##############################################################
#Plotting


l0 = []
l1 = []
l2 = []
l3 = []

for i in range(len(good_points)):
    if good_points[i][0] == 0:
        l0.append([good_points[i][1],good_points[i][2]])
    elif good_points[i][0] == 1:
        l1.append([good_points[i][1],good_points[i][2]])
    elif good_points[i][0] == 2:
        l2.append([good_points[i][1],good_points[i][2]])
    elif good_points[i][0] == 3:
        l3.append([good_points[i][1],good_points[i][2]])


fig1, axes1 = plt.subplots()
axes1.scatter([l0[i][1] for i in range(len(l0))],[l0[i][0] for i in range(len(l0))])
axes1.scatter([l1[i][1] for i in range(len(l1))],[l1[i][0] for i in range(len(l1))])
axes1.scatter([l2[i][1] for i in range(len(l2))],[l2[i][0] for i in range(len(l2))])
axes1.scatter([l3[i][1] for i in range(len(l3))],[l3[i][0] for i in range(len(l3))])
axes1.set_ylabel('Energy')
axes1.set_xlabel('r')
axes1.set_title("Energy Orbitals", va='bottom')
axes1.legend(('l=0','l=1','l=2', 'l=3'), loc='upper right')
plt.show()


