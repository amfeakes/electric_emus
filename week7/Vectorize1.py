#!/usr/bin/env python3
"""sum over all elements of a matrix and compare their time"""

__appname__ = 'Vectorize1.py'
__author__ = 'Xuanyin Zheng(xz1322@ic.ac.uk)'
__date___ = '2022.11'
__version__ = '0.0.1'

###import the necessary packages###
import numpy as np
import time as time

### Create a 1000×1000 matrix and fill it with random numbers###
"""M <- matrix(runif(1000000),1000,1000)"""

M = np.random.rand(1000,1000)

### Using loops: Create a function that sums all elements in matrix #####
"""SumAllElements <- function(M) {
  Dimensions <- dim(M)
  Tot <- 0
  for (i in 1:Dimensions[1]) {
    for (j in 1:Dimensions[2]) {
      Tot <- Tot + M[i,j]
    }
  }
  return (Tot)
}"""
def SumAllElements(M):
    tot = 0
    for i in np.nditer(M):
        tot = tot + i
    return tot





###Using the in-built vectorized function: Create a function that sums all elements in matrix###
def SumAllElements2(M):
    tot2 = np.sum(M)
    return tot2

###Calculate the operation time of each function###
start1 = time.time()
SumAllElements(M)
end1 = time.time()

start2 = time.time()
SumAllElements2(M)
end2 = time.time()

###print results of using loops and using the in-built vectorized function###
"""print("Using loops, the time taken is:")
print(system.time(SumAllElements(M)))
print("Using the in-built vectorized function, the time taken is:")
print(system.time(sum(M)))"""
print("Use loops to calculate the speed of each element sum of the matrix:")
print(end1 - start1)
print("Use the in-built vetorized to calculate the speed of each element sum of the matrix:")
print(end2 - start2)