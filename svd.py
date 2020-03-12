#svd decomposition A=U*S*transpose(V)

import numpy as np

import time

A=np.array([[0, 1, 1], [0, 1, 0], [1, 1, 0], [0, 1, 0], [1, 0, 1]])

start_time1=time.time()

#evaluating U
u1,U1=np.linalg.eigh(np.matmul(A,np.transpose(A)))
n=u1.size
u=np.zeros(n)
U=np.zeros((n,n))
for i in range(n):
    u[-i-1]=u1[i]
    for j in range(n):
        U[j][-i-1]=U1[j][i]

#evaluating V        
v1,V1=np.linalg.eigh(np.matmul(np.transpose(A),A))
m=v1.size
v=np.zeros(m)
V=np.zeros((m,m))
for k in range(m):
    v[-k-1]=v1[k]
    for l in range(m):
        V[l][-k-1]=V1[l][k]

print('using my code:')
print('S=',np.matmul(np.matmul(np.transpose(U),A),V))
print('U=',U)
print('V=',V)


stop_time1=time.time()

print('the required time is ',(time.time()- start_time1))

start_time2=time.time()

U_1,S_1,V_1=np.linalg.svd(A)

print('using numpy.linalg.svd:')
print('S=',S_1)
print('U=',U_1)
print('V=',V_1)

stop_time2=time.time()

print('the required time is ',(time.time()- start_time2))