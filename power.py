# -*- coding: utf-8 -*-
"""

@author: nabendu
"""

#power method AX=kX

import numpy as np

A=np.array([[2,-1,0],[-1,2,-1],[0,-1,2]])

X=np.array([1,0,0]) #starting vector

Y=np.zeros(3)

ESP=0.01 #error tolerance

MAXIT=100 #maximum iteration permitted

key=1

count=0

for i in range(MAXIT):
    if(key==1):
        k=0
        for j in range(3):
            sum=0
            for m in range(3):
                sum=sum+A[j][m]*X[m]
                Y[j]=sum
                if(abs(k)<abs(Y[j])):
                    k=Y[j]
        count=count+1
    else:
        break
    X1=Y/k
    #accuracy condition:
    key=0
    for n in range(3):
        if(abs(X1[n]-X[n])>ESP):
            key=1  
    X=X1

if(key==1):
    print('dominant eigen value=',k,'corresponding eigen vector:',X,'The required accuracy is not reached after ',count,' iterations')
else:
    print('dominant eigen value=',k,'corresponding eigen vector:',X,'iterations=',count)
