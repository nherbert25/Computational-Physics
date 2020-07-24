#Cromer Algorithm

import numpy as np
import matplotlib.pyplot as plt

def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)

def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)


################################

x_0 = 10
y_0 = -50
v_int = 1/10

#initial conditions
# r_0 = [(float(10), float(0))]
# v_0 = [(float(0), float(1/10))]

r_0 = [(x_0, 0)]
v_0 = [(0, v_int)]

r = r_0
v = v_0


############################################
#Other Constants

h = x_0*v_int
p = h**2
E_0 = .5*v_int**2-1/x_0
a = -1/(2*E_0)
e = (1-p/a)**.5
P = 2*np.pi*a**(3/2)
t = P/1000

# print('x_0 =',x_0,'\r\nv_int =',v_int,'\r\nr_0 =',r_0,'\r\nv_0 =',v_0,'\r\nh =',h,'\r\np =',p)
# print('E_0 =',E_0,'\r\na =',a,'\r\ne =',e)
# print('P =',P,'t =',t)

##############################################
#Algorithm


for i in range(0,int(P*100)):
	r_mag = (r[len(r)-1][0]**2+r[len(r)-1][1]**2)**.5
	acc = np.asarray((-r[len(r)-1][0]/r_mag**3,-r[len(r)-1][1]/r_mag**3))
		
	v.append(tuple(map(sum, zip(v[len(v)-1],acc*t))))
	v_add = np.asarray(v[len(v)-1])
	r.append(tuple(map(sum, zip(r[len(r)-1],v_add*t))))

r = np.asarray(r)

l = []
for i in r:
	l.append(cart2pol(i[0],i[1]))

x_val = [x[0] for x in l]
y_val = [x[1] for x in l]


##############################################
#Exact Solution

theta_ex = np.arange(0, 2*np.pi+.01, 0.1)
r_ex = p/(1-e*np.cos((theta_ex)))


#################################################################
#Graphing - Polar 

fig1, ax = plt.subplots()
ax = plt.subplot(111, projection='polar')
ax.plot(y_val,x_val)
ax.plot(theta_ex, r_ex, 'o', markerfacecolor='none', markeredgecolor='r')
ax.set_rmax(.5)
ax.set_rticks([3, 6, 9, 12])  # less radial ticks
ax.set_rlabel_position(-22.5)  # get radial labels away from plotted line
ax.grid(True)

ax.set_title("Cromer Algorithm", va='bottom')
# plt.show()


###################################################
#Energy

r_mag = []
v_mag = []
E_t = []
time = []
timePeriod = []
E_rat = []
for i in r:
	r_mag.append((i[0]**2+i[1]**2)**.5)
for i in v:
	v_mag.append((i[0]**2+i[1]**2)**.5)
for i in range(len(r_mag)):
	E_t.append(.5*v_mag[i]**2-1/r_mag[i])
for i in range(0,int(P*100)+1):
	x = i*t
	time.append(x)
for i in time:
	x = i/P
	timePeriod.append(x)
for i in range(len(E_t)):
	E_rat.append(E_t[i]/E_0-1)

#4.5 to 5.5
# print(timePeriod[430],timePeriod[440],timePeriod[450],timePeriod[550],timePeriod[570])

E_rat = E_rat[450:550]
timePeriod = timePeriod[450:550]

fig2, ax2 = plt.subplots()
ax2.plot(timePeriod,E_rat)
ax2.set_ylabel('E(t)/E_0-1')
ax2.set_xlabel('Time/Period')
ax2.set_title("Energy Ratio")
plt.show()


