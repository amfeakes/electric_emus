#!/usr/bin/env python3

"""This script vectorizes stochastic Ricker function under Python."""


_appname_ = 'Vectorize2'
__author__ = 'Electric Emus (amy.feakes22@imperial.ac.uk, f.ferreira22@imperial.ac.uk,\
                             zitong.zhao22@imperial.ac.uk, xuanyin.zheng22@imperial.ac.uk,\
                             dongxuan.zhu22@imperial.ac.uk)'
__version__ = '0.0.1'

#### imports ####
import numpy as np 
import timeit
from math import exp
 
#### functions ####
def stochrick(p0=np.random.uniform(low=.5,high=1.5,size=1000), r=1.2, K=1, sigma=.2,numyears=100):
    """An equivalent version of vectorization with pre-allocation in R."""
    N = np.zeros([numyears,len(p0)])
    N[0,] = p0

    for pop in range(len(p0)):
        for yr in range(1,numyears):
            N[yr,pop] = N[yr-1, pop] * exp(r * (1 - N[yr-1, pop] / K + np.random.normal(0,sigma,1)))
    
    return N 

def stochrickForm(p0, pop, numyears, r, K, sigma):
    """Stochastic Ricker's formula for later application."""
    N = np.zeros(numyears)
    N[0] = p0[pop]

    for yr in range(1,numyears):
        N[yr] = N[yr-1] * exp(r * (1 - N[yr-1] / K) + np.random.normal(0, sigma,1))
    
    return N

def stochrickvect(p0=np.random.uniform(low=.5,high=1.5,size=1000), r = 1.2, K = 1, sigma = 0.2,numyears = 100):
    """An equivalent version of vectorization with sapply in R."""
    
    result = [stochrickForm(p0,pop,numyears,r,K,sigma) for pop in np.arange(len(p0))]
    
    return result

#### outputs ####
vect2_time1 = timeit.timeit(stmt='stochrick()',globals = globals(), number=1)
vect2_time2 = timeit.timeit(stmt='stochrickvect()',globals = globals(), number=1)

print("\nIn python, the original vectorized stochastic Ricker function takes:")
print(vect2_time1)

print("In python, the modified vectorized stochastic Ricker function takes:")
print(vect2_time2)