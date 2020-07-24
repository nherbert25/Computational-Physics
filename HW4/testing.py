import numpy as np
import matplotlib.pyplot as plt
import useful as use
import pdb
np.set_printoptions(threshold=np.inf)

r = np.asarray([8,3,0])
v = np.asarray([4,5,0])
B = np.asarray([0,0,1/r[0]**2])
B_unit = B/np.linalg.norm(B)
dt = .05
theta = B[2]*dt


print("B vector",B)
print("cross product",np.cross(B,v))
print("unit vector of B",B_unit)



print(v+np.sin(theta)*np.cross(B_unit,v)+(1-np.cos(theta))*np.cross(B_unit,np.cross(B_unit,v)))


def v_calc(r, v, B, dt):
	theta = B[2]*dt
	B_unit = B/np.linalg.norm(B)
	
	return(v+np.sin(theta)*np.cross(B_unit,v)+(1-np.cos(theta))*np.cross(B_unit,np.cross(B_unit,v)))
	
print(v_calc(r, v, B, dt))