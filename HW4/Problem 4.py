import numpy as np
import matplotlib.pyplot as plt
import useful as use
import pdb
np.set_printoptions(threshold=np.inf)


fig1, ax3 = plt.subplots()
################################
#initial conditions

#stationary objects
r1 = np.asarray([-.5,0])
r2 = np.asarray([.5,0])

#trajectory object
# x_0 = 0.01
# y_0 = 0.058
# v_0 = [(.47, .01)]


x_0 = 0.02
y_0 = 0.058
v_int = 1
theta_int = np.radians(45)


r_0 = [(x_0, y_0)]
# v_0 = [(v_int*np.cos(theta_int), v_int*np.sin(theta_int))]
v_0 = [(.46, .02)]

r = r_0
v = v_0

h = x_0*v_int
p = h**2

# E_0 = .5*v_int**2-1/x_0
# a = -1/(2*E_0)
# e = (1-p/a)**.5
# P = 2*np.pi*a**(3/2)
t = 0
dt = .005
s = 2**(1/3)
H = dt/(2-s)



##############################################
#Fourth-Order Forest Ruth
# x_0 = 10
# y_0 = -50
# v_int = 1/10

# r_0 = [(x_0, 0)]
# v_0 = [(0, v_int)]

# r = r_0
# v = v_0
# A_x = []
# A_y = []


for i in range(0,int((9*np.pi)/dt)):
	v_n = np.asarray(v[len(v)-1])
	r_n = np.asarray(r[len(r)-1])
	
	

	r_n = use.int_q_array(r_n, v_n, .5*H)
	t = t +.5*H
	r1 = np.asarray([-.5*np.cos(t), -.5*np.sin(t)])
	r2 = np.asarray([.5*np.cos(t),.5*np.sin(t)])


	v_n = use.int_v_array(r_n, r1, r2, v_n, H)
	r1 = np.asarray([-.5*np.cos(t), -.5*np.sin(t)])
	r2 = np.asarray([.5*np.cos(t),.5*np.sin(t)])


	r_n = use.int_q_array(r_n, v_n, .5*H)
	t = t +.5*H
	r1 = np.asarray([-.5*np.cos(t), -.5*np.sin(t)])
	r2 = np.asarray([.5*np.cos(t),.5*np.sin(t)])



####################################################################

	r_n = use.int_q_array(r_n, v_n, -.5*s*H)
	t = t - .5*s*H
	r1 = np.asarray([-.5*np.cos(t), -.5*np.sin(t)])
	r2 = np.asarray([.5*np.cos(t),.5*np.sin(t)])


	v_n = use.int_v_array(r_n, r1, r2, v_n, -s*H)
	r1 = np.asarray([-.5*np.cos(t), -.5*np.sin(t)])
	r2 = np.asarray([.5*np.cos(t),.5*np.sin(t)])


	r_n = use.int_q_array(r_n, v_n, -.5*s*H)
	t = t - .5*s*H
	r1 = np.asarray([-.5*np.cos(t), -.5*np.sin(t)])
	r2 = np.asarray([.5*np.cos(t),.5*np.sin(t)])




##########################################################################


	r_n = use.int_q_array(r_n, v_n, .5*H)
	t = t +.5*H
	r1 = np.asarray([-.5*np.cos(t), -.5*np.sin(t)])
	r2 = np.asarray([.5*np.cos(t),.5*np.sin(t)])


	v_n = use.int_v_array(r_n, r1, r2, v_n, H)
	r1 = np.asarray([-.5*np.cos(t), -.5*np.sin(t)])
	r2 = np.asarray([.5*np.cos(t),.5*np.sin(t)])


	r_n = use.int_q_array(r_n, v_n, .5*H)
	t = t +.5*H
	r1 = np.asarray([-.5*np.cos(t), -.5*np.sin(t)])
	r2 = np.asarray([.5*np.cos(t),.5*np.sin(t)])



	r.append(r_n)
	v.append(v_n)
	# print(r1,r1[0],r1[1])
	# pdb.set_trace()
	# ax3.plot([r1[0],r1[1]], 'o', markerfacecolor='none', markeredgecolor='r')
	# ax3.plot([r1], 'o', markerfacecolor='none', markeredgecolor='r')


r = np.asarray(r)
l = []

x_val = [x[0] for x in r]
y_val = [x[1] for x in r]


###################################################
#Graphing 

# fig1, ax3 = plt.subplots()
ax3.plot(x_val,y_val)
ax3.set_ylabel('Y Coordinate')
ax3.set_xlabel('X Coordinate')
# ax3.plot([-.5,.5], [0,0], 'o', markerfacecolor='none', markeredgecolor='r')
ax3.set_title("2D Time Dependent Two-Center Gravitational: T4 Forest Ruth", va='bottom')
# plt.show()






timing = []
for i in range(len(x_val)):
	timing.append(i*dt)
	# print(timing)
	# if i >5:
		# exit()
timing = np.asarray(timing)


# for i in range(20):
# print(np.cos(timing)*x_val*np.sin(timing)*y_val, -np.sin(timing)*x_val*np.cos(timing)*y_val)


fig2, ax4 = plt.subplots()
ax4.plot(np.cos(timing)*x_val+np.sin(timing)*y_val, -np.sin(timing)*x_val+np.cos(timing)*y_val)
# ax4.plot(np.cos(np.radians(timing))*x_val*np.sin(np.radians(timing))*y_val, -np.sin(np.radians(timing))*x_val*np.cos(np.radians(timing))*y_val)
ax4.set_ylabel('Y Coordinate')
ax4.set_xlabel('X Coordinate')
ax4.set_title("Chaotic Fourth Order FR: Co-rotating Frame", va='bottom')
plt.show()








"""

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

"""