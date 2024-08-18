# -*- coding: utf-8 -*-
"""
Spyder Editor

Author @Pooja H
"""

#%%
import numpy as np
from sympy import *

#%%
# Reading the matrix data

A = Matrix([[3, -2], [4, -2]])
print("\nThe given matrix is:\n",A)

#%%
#Compute the value of k, with k as a variable
k= var('k')
lhs = A.multiply(A) + 2*np.identity(2)
rhs = k*A 
result = Eq(rhs[0,0],lhs[0,0])
print("\n The value of k is:")
print(solve(result, k))

