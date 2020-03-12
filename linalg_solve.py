# -*- coding: utf-8 -*-

import numpy as np
from numpy.linalg import solve

A=np.array([[1,0.67,0.33],[0.45,1,0.55],[0.67,0.33,1]])

v=np.array([2.0,2,2])

print(solve(A,v))