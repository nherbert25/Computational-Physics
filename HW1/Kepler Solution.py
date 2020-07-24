#Kepler Solution

import numpy as np
import matplotlib.pyplot as plt


################################

x_0 = 10
y_0 = -50
v_int = 1/10


#initial conditions
r_0 = (x_0, 0)
v_0 = (0, v_int)


h = x_0*v_int
p = h**2
E_0 = .5*v_int**2-1/x_0
a = -1/(2*E_0)
e = (1-p/a)**.5
P = 2*np.pi*a**(3/2)

# print('x_0 =',x_0,'\r\nv_int =',v_int,'\r\nr_0 =',r_0,'\r\nv_0 =',v_0,'\r\nh =',h,'\r\np =',p)
# print('E_0 =',E_0,'\r\na =',a,'\r\ne =',e)


##############################################
#Exact Solution

theta = np.arange(0, 2*np.pi+.01, 0.01)
r = p/(1-e*np.cos((theta)))

#############################################################
#Graphing Exact Solution

ax = plt.subplot(111, projection='polar')
# ax.plot(theta, r, 'o', markerfacecolor='none', markeredgecolor='r')
ax.plot(theta, r)
ax.set_rmax(.5)
ax.set_rticks([3, 6, 9, 12])  # less radial ticks
ax.set_rlabel_position(-22.5)  # get radial labels away from plotted line
ax.grid(True)

ax.set_title("Kepler Solution", va='bottom')
plt.show()

#################################################################





