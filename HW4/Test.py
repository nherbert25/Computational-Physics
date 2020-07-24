import numpy as np

l = []
r_0 = np.array((1,0,0))
v_0 = np.array((0,0,0))
t = 0
r = r_0
v = v_0
s = 2**(1/3)
# H = dt[j]/(2-s)
w_0 = 1
gamma=.6
w = np.sqrt(w_0**2-gamma**2)

t=40
# for i in range(0,int(20*2*np.pi/dt)):



print(np.e**(-gamma*0))
print(np.e**(-gamma*2))
print(np.e**(-gamma*12))



def timing(t):
	r_n = np.e**(-gamma*t)*(r_0*np.cos(w*t)+(v_0+gamma*r_0)/w*np.sin(w*t))
	print(r_n)
	
	
timing(40)
timing(80)


timing(np.pi/w*5/2)
timing(np.pi/w*7/2)
timing(np.pi/w*11/2)
timing(np.pi/w*25/2)