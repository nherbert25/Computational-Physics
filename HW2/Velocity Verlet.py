#Velocity Verlet Algorithm

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

x_0 = 10
y_0 = -50
v_int = 1/10

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

##############################################
#Algorithm for t



for i in range(0,int(P*100)):
	r_add = np.asarray(r[len(r)-1])
	v_add = np.asarray(v[len(v)-1])
	r_mag = (r_add[0]**2+r_add[1]**2)**.5
	acc = np.asarray((-r_add[0]/r_mag**3,-r_add[1]/r_mag**3))
	r.append(tuple(map(sum, zip(r_add,v_add*t,.5*t**2*acc))))
	r_mag2 = (r[len(r)-1][0]**2+r[len(r)-1][1]**2)**.5
	acc_2 = np.asarray((-r[len(r)-1][0]/r_mag2**3,-r[len(r)-1][1]/r_mag2**3))
	v.append(tuple(map(sum, zip(v[len(v)-1],.5*t*acc,.5*t*acc_2))))






# for i in range(0,int(P*100)):
	# r_mag = (r[len(r)-1][0]**2+r[len(r)-1][1]**2)**.5
	# acc = np.asarray((-r[len(r)-1][0]/r_mag**3,-r[len(r)-1][1]/r_mag**3))
	# v_add = np.asarray(v[len(v)-1])
	# r_add = np.asarray(r[len(r)-1])
	# r.append(tuple(map(sum, zip(r[len(r)-1],v_add*t,.5*t**2*acc))))
	# r_mag2 = (r[len(r)-1][0]**2+r[len(r)-1][1]**2)**.5
	# acc_2 = np.asarray((-r[len(r)-1][0]/r_mag2**3,-r[len(r)-1][1]/r_mag2**3))
	# v.append(tuple(map(sum, zip(v[len(v)-1],.5*t*acc,.5*t*acc_2))))
		
r = np.asarray(r)


##############################################
#Algorithm for t/2
x_0 = 10
y_0 = -50
v_int = 1/10

r_0 = [(x_0, 0)]
v_0 = [(0, v_int)]

r_2 = r_0
v_2 = v_0

# print(r_0,v_0,r_2,v_2)


t_2 = t/2



for i in range(0,int(P*100)):
	r_add = np.asarray(r[len(r_2)-1])
	v_add = np.asarray(v[len(v_2)-1])
	r_mag = (r_add[0]**2+r_add[1]**2)**.5
	acc = np.asarray((-r_add[0]/r_mag**3,-r_add[1]/r_mag**3))
	r_2.append(tuple(map(sum, zip(r_add,v_add*t_2,.5*t_2**2*acc))))
	r_mag2 = (r_2[len(r_2)-1][0]**2+r_2[len(r_2)-1][1]**2)**.5
	acc_2 = np.asarray((-r_2[len(r_2)-1][0]/r_mag2**3,-r_2[len(r_2)-1][1]/r_mag2**3))
	v.append(tuple(map(sum, zip(v_2[len(v_2)-1],.5*t_2*acc,.5*t_2*acc_2))))

















# for i in range(0,int(P*100)):
	# v_add = np.asarray(v_2[len(v_2)-1])
	# r_add = np.asarray(r_2[len(r_2)-1])

	# r_mag = (r_2[len(r_2)-1][0]**2+r_2[len(r_2)-1][1]**2)**.5
	# acc = np.asarray((-r_2[len(r_2)-1][0]/r_mag**3,-r_2[len(r_2)-1][1]/r_mag**3))

	# r_2.append(tuple(map(sum, zip(r_2[len(r_2)-1],v_add*t_2,.5*t_2**2*acc))))
	# r_mag2 = (r_2[len(r_2)-1][0]**2+r_2[len(r_2)-1][1]**2)**.5
	# acc_2 = np.asarray((-r_2[len(r_2)-1][0]/r_mag2**3,-r_2[len(r_2)-1][1]/r_mag2**3))
	# v.append(tuple(map(sum, zip(v_2[len(v_2)-1],.5*t_2*acc,.5*t_2*acc_2))))
		
r_2 = np.asarray(r_2)

# print(r_2)
##############################################################
#function for adding both plots together


# print(len(r),len(r_2))

# print(r)

r_total = [4/3*r_2-1/3*r]
# print("r_tot = ",len(r_total[0]))

l = []
for i in range(len(r_total[0])):
	l.append(cart2pol(r_total[0][i][0],r_total[0][i][1]))


# l = []
# for i in range(len(r_total[0])):
	# l.append(cart2pol(r_total[0][i][0],r_total[0][i][1]))

# l = []
# for i in r_2:
	# l.append(cart2pol(i[0],i[1]))

x_val = [x[0] for x in l]
y_val = [x[1] for x in l]

# print("x_val = ",x_val)


##############################################
#Exact Solution

# theta_ex = np.arange(0, 2*np.pi+.01, 0.1)
# r_ex = p/(1-e*np.cos((theta_ex)))


#################################################################
#Graphing - Polar 


fig1, ax = plt.subplots()
ax = plt.subplot(111, projection='polar')
ax.plot(y_val,x_val)
# ax.plot(theta_ex, r_ex, 'o', markerfacecolor='none', markeredgecolor='r')
ax.set_rmax(.5)
ax.set_rticks([3, 6, 9, 12])  # less radial ticks
ax.set_rlabel_position(-22.5)  # get radial labels away from plotted line
ax.grid(True)

ax.set_title("Velocity Verlet", va='bottom')
# plt.show()


###################################################
#Energy


# r_mag = np.asarray([])
r_mag = []
v_mag = []
E_t = []
time = []
for i in r:
	# print(i)
	# print(i[0])
	# print((i[0]**2+i[1]**2)**.5)
	r_mag.append((i[0]**2+i[1]**2)**.5)
for i in v:
	# print((i[0]**2+i[1]**2)**.5)
	v_mag.append((i[0]**2+i[1]**2)**.5)
for i in range(len(r_mag)):
	# print(.5*v_mag[i]**2-1/r_mag[i])
	E_t.append(.5*v_mag[i]**2-1/r_mag[i])
for i in range(0,int(P*100)+1):
	x = i*t
	time.append(x)


# print(r_mag[0],r_mag[1],r_mag[100],r_mag[50],r_mag[20],r_mag[1000])
# print(v_mag[0],v_mag[1],v_mag[100],v_mag[50],v_mag[20],v_mag[1000])
# print(time)
# print(E_t)
# print(E_t[0])
# E_t = np.array(E_t)
# E_t = np.array(E_t)

# E_t = np.asarray(E_t)

E_rat = []
for i in range(len(E_t)):
	# print(E_t(i))
	E_rat.append(E_t[i]/E_0-1)
	
# print(E_rat)



fig2, ax2 = plt.subplots()
ax2.plot(time,E_rat)
ax2.set_ylabel('Energy')
ax2.set_xlabel('Time')
plt.show()