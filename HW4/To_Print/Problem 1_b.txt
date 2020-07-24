import numpy as np
import matplotlib.pyplot as plt
import useful as use
import pdb
np.set_printoptions(threshold=np.inf)


fig1, ax3 = plt.subplots()
################################
#initial conditions

dt = [.4,.2,.1]

##############################################
#Fourth-Order Forest Ruth


for j in range(len(dt)):
	r_0 = [(1,0,0)]
	v_0 = [(0,.5,0)]
	t = 0
	r = r_0
	v = v_0
	s = 2**(1/3)
	H = dt[j]/(2-s)

	for i in range(0,int((6*np.pi)/dt[j])):
		v_n = np.asarray(v[len(v)-1])
		r_n = np.asarray(r[len(r)-1])

		#############
		r_n = use.int_q_array(r_n, v_n, .5*H)
		B = np.asarray([0,0,1/r_n[0]**2])
		v_n = use.v_magnetic_calc(r_n, v_n, B, H)
		r_n = use.int_q_array(r_n, v_n, .5*H)
		##############
		r_n = use.int_q_array(r_n, v_n, -.5*s*H)
		B = np.asarray([0,0,1/r_n[0]**2])
		v_n = use.v_magnetic_calc(r_n, v_n, B, -s*H)
		r_n = use.int_q_array(r_n, v_n, -.5*s*H)
		#############
		r_n = use.int_q_array(r_n, v_n, .5*H)
		B = np.asarray([0,0,1/r_n[0]**2])
		v_n = use.v_magnetic_calc(r_n, v_n, B, H)
		r_n = use.int_q_array(r_n, v_n, .5*H)
		##############
		r.append(r_n)
		v.append(v_n)

	r = np.asarray(r)
	x_val = [x[0] for x in r]
	y_val = [x[1] for x in r]
	ax3.plot(x_val,y_val)


###################################################
###################################################
#graphing
ax3.set_ylabel('Y Coordinate')
ax3.set_xlabel('X Coordinate')
ax3.legend(('dt = .4','dt = .2','dt = .1'), loc='upper right')
ax3.set_title("Particle Trajectory - T4 Algorithm", va='bottom')
plt.show()