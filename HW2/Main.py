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
	
def sum2(x, y):
	return tuple(map(sum, zip(x,y)))

def sum3(x, y, z):
	return tuple(map(sum, zip(x,y, z)))

################################
#initial conditions

x_0 = 10
y_0 = 0
v_int = 1/10

r_0 = [(x_0, y_0)]
v_0 = [(0, v_int)]

r = r_0
v = v_0

h = x_0*v_int
p = h**2
E_0 = .5*v_int**2-1/x_0
a = -1/(2*E_0)
e = (1-p/a)**.5
P = 2*np.pi*a**(3/2)
t = P/1000



##############################################
#Runge-Kutta
x_0 = 10
y_0 = -50
v_int = 1/10

r_0 = [(x_0, 0)]
v_0 = [(0, v_int)]

r = r_0
v = v_0



# r_n1
# v_n1

#

for i in range(0,int(P*100)):
	v_n = np.asarray(v[len(v)-1])  #this is v_n
	r_n = np.asarray(r[len(r)-1])  #this is r_n
	
	r_mag = (r_n[0]**2+r_n[1]**2)**.5  #magnitude of r_n, used to calculate a_n
	a_n = np.asarray((-r_n[0]/r_mag**3,-r_n[1]/r_mag**3))  #this is a_n
	
	
	#r_n1 (the midpoint estimate, used for calculating a_n1)
	r_n1 = np.asarray(sum3(r_n, .5*t*v_n, 1/8*t**2*a_n))
	r_n1_mag = (r_n1[0]**2+r_n1[1]**2)**.5
	a_n1 = np.asarray((-r_n1[0]/r_n1_mag**3,-r_n1[1]/r_n1_mag**3))
	
	r_add = sum3(r_n, t*v_n, sum2(t**2/6*a_n,t**2/6*2*a_n1))

	
	r_n2 = sum3(r_n, t*v_n, .5*t**2*a_n1)
	r_n2_mag = (r_n2[0]**2+r_n2[1]**2)**.5
	a_n2 = np.asarray((-r_n2[0]/r_n2_mag**3,-r_n2[1]/r_n2_mag**3))
	v_add = sum2(v_n, sum3(t/6*a_n, t/6*4*a_n1, t/6*a_n2))
	
	r.append(r_add)
	v.append(v_add)


r = np.asarray(r)
l = []

for i in r:
	l.append(cart2pol(i[0],i[1]))

x_val = [x[0] for x in l]
y_val = [x[1] for x in l]

#Graphing 

fig1, ax3 = plt.subplots()
ax3=fig1.add_subplot(111, projection='polar')
ax3.plot(y_val,x_val)
# ax3.plot(theta_comp, r_comp, 'o', markerfacecolor='none', markeredgecolor='r')
ax3.set_rmax(.5)
ax3.set_rticks([3, 6, 9, 12])  # less radial ticks
ax3.set_rlabel_position(-22.5)  # get radial labels away from plotted line
ax3.grid(True)
ax3.set_title("Runge-Kutta", va='bottom')
plt.show()