# -*- coding: utf-8 -*-
"""

@author: nabendu
"""

#QR decomposition

import numpy as np

A=np.array([[5,-2],[-2,8]])

a,X=np.linalg.eigh(A) #h in eigh for hermitian

for i in range(100):
    Q,R=np.linalg.qr(A) #QR decomposition
    A=np.matmul(np.transpose(Q),np.matmul(A,Q))
    #accuracy condition:
    key=0
    for i in range(2):
        for j in range(2):
            if(i!=j):
                if(abs(A[i][j])>0.0001):
                    key=1
    if(key==0):
        break

a1=np.zeros(2)

for j in range(2):
    a1[j]=A[j][j]
    
print('eigenvalues using eigh:',a,'eigenvalues using QR:',a1)