import numpy as np
import useful as use

r = np.array([3,3])
r1 = np.array([.5,0])
r2 = np.array([-.5,0])


rtot1 = r-r1
rtot2 = r-r2




print(use.mag_multi(r1,r)+use.mag_multi(r2,r))
print(use.mag_array(rtot1)+use.mag_array(rtot2))
print(use.mag((r-r1)[0],(r-r1)[1])+use.mag((r-r2)[0],(r-r2)[1]))





print(use.acc_multi(r,r1,r2))
print(use.acc_array(rtot1)+use.acc_array(rtot2))
print(np.array(use.acc((r-r1)[0],(r-r1)[1]))+np.array(use.acc((r-r2)[0],(r-r2)[1])))

t=.01
r_n = np.array([.25,.5])
v_n = np.array([1,1])

print('originals',r_n,v_n)
r_n = use.int_q_array(r_n, v_n, .5*t)
print('r1',r_n)
v_n = use.int_v_array(r_n, r1, r2, v_n, t)
print('v1',v_n)
r_n = use.int_q_array(r_n, v_n, .5*t)
print('r2',r_n)