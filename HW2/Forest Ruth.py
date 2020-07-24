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
	return(q3,q4)
	
def int_v(q1,q2,v1,v2,t):
	v3 = v1 + t*acc(q1,q2)[0]
	v4 = v2 + t*acc(q1,q2)[1]
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
s = 2**(1/3)
H = t/(2-s)



##############################################
#Fourth-Order Forest Ruth
x_0 = 10
y_0 = -50
v_int = 1/10

r_0 = [(x_0, 0)]
v_0 = [(0, v_int)]

r = r_0
v = v_0
A_x = []
A_y = []


for i in range(0,int(P*100)):
	v_n = np.asarray(v[len(v)-1])
	r_n = np.asarray(r[len(r)-1])
	
	
	r_n = int_q(r_n[0],r_n[1], v_n[0], v_n[1], H/2)
	v_n = int_v(r_n[0],r_n[1], v_n[0], v_n[1], H)
	r_n = int_q(r_n[0],r_n[1], v_n[0], v_n[1], H/2*(1-s))
	v_n = int_v(r_n[0],r_n[1], v_n[0], v_n[1], -s*H)
	
	r_n = int_q(r_n[0],r_n[1], v_n[0], v_n[1], H/2*(1-s))
	v_n = int_v(r_n[0],r_n[1], v_n[0], v_n[1], H)
	r_n = int_q(r_n[0],r_n[1], v_n[0], v_n[1], H/2)
	
	
	A_x_add = v_n[1]*(r_n[0]*v_n[1]-v_n[0]*r_n[1])-r_n[0]/mag(r_n[0],r_n[1])
	A_y_add = v_n[0]*(r_n[1]*v_n[0]-v_n[1]*r_n[0])-r_n[1]/mag(r_n[0],r_n[1])
	
	# print(A_x_add, A_y_add)
	# print(A_x, A_y)
	
	r.append(r_n)
	v.append(v_n)
	A_x.append(A_x_add)
	A_y.append(A_y_add)

	
r = np.asarray(r)
l = []

# for i in r:
	# l.append(cart2pol(i[0],i[1]))

x_val = [x[0] for x in r]
y_val = [x[1] for x in r]


###################################################
#Graphing 

fig1, ax3 = plt.subplots()
# ax3=fig1.add_subplot(111, projection='polar')
# ax3=fig1.add_subplot(111)
ax3.plot(y_val,x_val)
# ax3.plot(theta_comp, r_comp, 'o', markerfacecolor='none', markeredgecolor='r')
# ax3.set_rmax(.5)
# ax3.set_rticks([3, 6, 9, 12])  # less radial ticks
# ax3.set_rlabel_position(-22.5)  # get radial labels away from plotted line
# ax3.grid(True)
ax3.set_title("Forest Ruth", va='bottom')
# plt.show()



###################################################
#Forest Ruth Energy

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
ax5.set_ylabel('(E(t)/E_0-1)/t^4')
ax5.set_xlabel('Time/Period')
ax5.set_title("Energy Ratio - Forest Ruth")
ax5.plot(timePeriod,E_rat)
plt.show()





#Computing A


m = []

cat = 0

for i in A_x:


	# print(A_y[cat], A_x[cat], np.arctan(A_y[cat]/A_x[cat]))
	m.append(np.arctan(A_y[cat]/A_x[cat])/t**4)
	
	cat+=1
	# print (m)
	# if cat > 5:
		# exit()

timing = []
for i in range(len(m)):
	timing.append(i*t)
	# print(timing)
	# if i >5:
		# exit()


fig3, ax6 = plt.subplots()
ax6.set_ylabel('theta/t^4')
ax6.set_xlabel('time')
ax6.set_title("theta/t^4 Plot Comparison")
ax6.plot(timing,m)
plt.show()