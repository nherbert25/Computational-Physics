import numpy as np
import matplotlib.pyplot as plt
import useful as use

################################
#initial conditions

#stationary objects
r1 = np.asarray([-.5,0])
r2 = np.asarray([.5,0])

#trajectory object
x_0 = 0
y_0 = 0
v_int = 1
theta_int = np.radians(45)

r_0 = [(x_0, y_0)]
v_0 = [(v_int*np.cos(theta_int), v_int*np.sin(theta_int))]

r = r_0
v = v_0

h = x_0*v_int
p = h**2

# E_0 = .5*v_int**2-1/x_0
# a = -1/(2*E_0)
# e = (1-p/a)**.5
# P = 2*np.pi*a**(3/2)
t = 1/1000
s = 2**(1/3)
H = t/(2-s)



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


for i in range(0,int(10000)):
	v_n = np.asarray(v[len(v)-1])
	r_n = np.asarray(r[len(r)-1])

	r_n = use.int_q_array(r_n, v_n, .5*t)
	v_n = use.int_v_array(r_n, r1, r2, v_n, t)
	r_n = use.int_q_array(r_n, v_n, .5*t)


	# if i > 9991:
		# print(r)
		# exit()
	# print('we made it through!!')
	
	r.append(r_n)
	v.append(v_n)


r = np.asarray(r)
l = []
x_val = [x[0] for x in r]
y_val = [x[1] for x in r]


###################################################
#Graphing 

fig1, ax3 = plt.subplots()
# ax3=fig1.add_subplot(111, projection='polar')
# ax3=fig1.add_subplot(111)
ax3.plot(x_val,y_val)
ax3.plot([-.5,.5], [0,0], 'o', markerfacecolor='none', markeredgecolor='r')
# ax3.set_rmax(.5)
# ax3.set_rticks([3, 6, 9, 12])  # less radial ticks
# ax3.set_rlabel_position(-22.5)  # get radial labels away from plotted line
# ax3.grid(True)
ax3.set_title("Forest Ruth", va='bottom')
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