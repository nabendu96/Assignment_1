# -*- coding: utf-8 -*-
"""

@author: nabendu
"""

#conjugate gradient method Ax=b

import numpy as np

A=np.array([[0.2,0.1,1,1,0],[0.1,4,-1,1,-1],[1,-1,60,0,-2],[1,1,0,8,4],[0,-1,-2,4,700]])

b=np.array([1,2,3,4,5])

x=np.zeros(5) #initial guess

y=np.array([7.859713071,0.422926408,-0.073592239,-0.540643016,0.010626163]) #true solution

r=b-np.matmul(A,x)
d=r

count=1

for h in range(100):
    s=np.matmul(np.transpose(r),r)/np.matmul(np.matmul(np.transpose(d),A),d)
    x=x+s*d
    r1=r-s*np.matmul(A,d)
    #checking accuracy
    key=0
    for k in range(5):            
        if(abs(x[k]-y[k])>=0.01):
            key=1
    if(key==0):
        break
    c=np.matmul(np.transpose(r1),r1)/np.matmul(np.transpose(r),r)
    r=r1
    d=r+c*d
    count=count+1

if(key==1):
    print('solution:',x,'The required accuracy is not reached after ',count,' iterations')
else:
    print('solution:',x,'iterations=',count)