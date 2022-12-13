#!/usr/bin/env python3
"""Whether with vectorization Stochastic (Gaus.) Ricker and compare their time"""

__appname__ = 'Vectorize2.py'
__author__ = 'Xuanyin Zheng(xz1322@ic.ac.uk)'
__date___ = '2022.11'
__version__ = '0.0.1'

###import the necessary packages###
import numpy as np
import time as time

# Runs the stochastic Ricker equation with gaussian fluctuations

def stochrick(p0 = np.random.uniform(.5, 1.5, 1000), r = 1.2, K = 1, sigma = 0.2,numyears = 100):

  N = np.full(numyears, len(p0))  #initialize empty matrix
  N[0, ] = p0
  for pop in range(1, p0, 1):#loop through the populations
    for yr in range(2, p0, 1): #for each pop, loop through the years
      N[yr, pop] = N[yr-1, pop] * np.exp(r * (1 - N[yr - 1, pop] / K) + np.random.normal(0, sigma)) # add one fluctuation from normal distribution
    
    return N 



# Now write another function called stochrickvect that vectorizes the above to
# the extent possible, with improved performance: 
def stochrickvect (p0 = np.random.uniform(.5, 1.5, 1000), r = 1.2, K = 1, sigma = 0.2,numyears = 100):

  N = np.full(numyears, len(p0))  #initialize empty matrix
  N[0, ] = p0 
  for yr in range(2, p0): #for each pop, loop through the years
      N[yr, ] = N[yr-1, ] * np.exp(r * (1 - N[yr - 1, ] / K) + np.random.normal(0, sigma)) # add one fluctuation from normal distribution   
      return N

###Calculate the operation time of each function###
start1 = time.time()
stochrick
end1 = time.time()

start2 = time.time()
stochrickvect
end2 = time.time()

print("original function takes:")
print(end1 - start1)
print("Vectorized Stochastic Ricker takes:")
print(end2 - start2)