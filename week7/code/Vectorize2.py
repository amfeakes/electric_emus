#!/usr/bin/env python3

"""This script vectorizes stochastic Ricker function under Python."""


_appname_ = 'Vectorize2'
_author_ = 'Dongxuan Zhu (dongxuan.zhu22@imperial.ac.uk)'
_version_ = '0.0.1'
_license_ = "N/A"

#### imports ####
import numpy as np 
import timeit
from math import exp
 
#### functions ####
def stochrick(p0 = np.random.uniform(low=.5,high=1.5,size=1000), r=1.2, K=1, sigma=.2,numyears=100):
    N = np.zeros([numyears,len(p0)])
    N[1,] = p0

    for pop in range(len(p0)):
        for yr in range(1,numyears):
            N[yr,pop] = N[yr-1, pop] * exp(r * (1 - N[yr-1, pop] / K + np.random.normal(0,sigma,1)))
    
    return N 


#### outputs ####
vect2_time = timeit.timeit(stmt='stochrick()',globals = globals(), number=1)

print("Using the vectorized stochastic Ricker function, the time taken is:")
print(vect2_time)
