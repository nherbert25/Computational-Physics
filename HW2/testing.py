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
	
def mag(x, y):
	return(np.sqrt(x**2+y**2))
	
def acc(x, y):
	return(-x/mag(x,y)**3, -y/mag(x,y)**3)

def int_q(q1,q2,v1,v2,t):
	q3 = q1 + t*v1
	q4 = q2 + t*v2
	# print('q3 = ',q3, ' q4 = ',q4)
	return(q3,q4)
	
def int_v(q1,q2,v1,v2,t):
	v3 = v1 + t*acc(q1,q2)[0]
	v4 = v2 + t*acc(q1,q2)[1]
	
	# print('v3 = ',v3, ' v4 = ',v4)
	return(v3,v4)

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
#Fourth-Order Runge-Kutta
x_0 = 10
y_0 = -50
v_int = 1/10

r_0 = [(x_0, 0)]
v_0 = [(0, v_int)]

r = r_0
v = v_0



# array([1, 2])
# >>> y = x+4
# >>> y
# array([5, 6])
# >>> z = np.append([y],[4,5])
# >>> z
# array([5, 6, 4, 5])
# >>> z = np.append([[y]],[4,5])
# >>> z
# array([5, 6, 4, 5])
# >>> z = np.append([y],[4,5],axis = 0)











for i in range(0,int(P*100)):
	v_n = np.asarray(v[len(v)-1])  #this is v_n
	r_n = np.asarray(r[len(r)-1])  #this is r_n
	
	

	# print('hello?',int_q(r_n[0],r_n[1], v_n[0], v_n[1], t/2))
	# print("int output",int_v(r_n[0],r_n[1], v_n[0], v_n[1], t))
	# exit()
	
	
	r_n = int_q(r_n[0],r_n[1], v_n[0], v_n[1], t/2)
	
	# print('r_n after first int = ',r_n)
	
	v_n = int_v(r_n[0],r_n[1], v_n[0], v_n[1], t)
	r_n = int_q(r_n[0],r_n[1], v_n[0], v_n[1], t/2)
	
	# print(r_n)
	# print('v_n',v_n)
		
	# if i > 5:
		# exit()
	
	# a_n = np.asarray(acc(r_n[0],r_n[1]))  #this is a_n
	# r_n1 = np.asarray(r_n + .5*t*v_n + 1/8*t**2*a_n)
	# r_n1_mag = (r_n1[0]**2+r_n1[1]**2)**.5
	# a_n1 = np.asarray((-r_n1[0]/r_n1_mag**3,-r_n1[1]/r_n1_mag**3))
	
	# r_add = r_n + t*v_n + (t**2/6*(a_n + 2*a_n1))
	
	# r_n2 = r_n + t*v_n + .5*t**2*a_n1
	# r_n2_mag = (r_n2[0]**2+r_n2[1]**2)**.5
	# a_n2 = np.asarray((-r_n2[0]/r_n2_mag**3,-r_n2[1]/r_n2_mag**3))
	# v_add = v_n + t/6*(a_n + 4*a_n1 + a_n2)
	
	r.append(r_n)
	v.append(v_n)
	# print(r)
	# exit()

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
ax3.set_title("Fourth-Order Runge-Kutta", va='bottom')
# plt.show()



###################################################
#Fourth-Order Runge-Kutta Energy

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
	E_rat.append((E_t[i]/E_0-1)/t**4)

E_rat = E_rat[450:550]
timePeriod = timePeriod[450:550]

fig2, ax5 = plt.subplots()
ax5.set_ylabel('E(t)/E_0-1')
ax5.set_xlabel('Time/Period')
ax5.set_title("Energy Ratio")
ax5.plot(timePeriod,E_rat)
plt.show()