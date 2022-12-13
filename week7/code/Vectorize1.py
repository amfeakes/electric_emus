#!/usr/bin/env python3

"""This script compares the speed of loops and in-built vectorized \
function under Python."""


_appname_ = 'Vectorize1'
_author_ = 'Dongxuan Zhu (dongxuan.zhu22@imperial.ac.uk)'
_version_ = '0.0.1'
_license_ = "N/A"

#### imports ####
import numpy as np 
import timeit


M = np.random.uniform(size=1000000).reshape(1000,1000)

 
#### functions ####
def SumAllElement(M):
    """Loop without vectorization."""
    Dimensions = M.shape
    Tot = 0
    for i in range(Dimensions[0]):
        for j in range(Dimensions[1]):
            Tot = Tot + M[i,j]

    return Tot

#### outputs ####
loop_time = timeit.timeit(stmt='SumAllElement(M)',globals = globals(), number=1)
vect_time = timeit.timeit(stmt='np.sum(M)',globals = globals(), number=1)

print("\nIn python, the sum function using loop takes:")
print(loop_time)

print("In python, the sum function with in-built vectorization takes:")
print(vect_time)
