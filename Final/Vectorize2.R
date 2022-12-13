#!/usr/bin/Rscript

# Script: Vectorize1.R
# Author: Electric Emus (dongxuan.zhu22@imperial.ac.uk, f.ferreira22@imperial.ac.uk, 
#                        amy.feakes22@imperial.ac.uk, zitong.zhao22@imperial.ac.uk,
#                        xuanyin.zheng22@imperial.ac.uk)
# Description: Runs the stochastic Ricker equation with gaussian fluctuations
# Date: Oct 2022


rm(list = ls())

stochrick <- function(p0 = runif(1000, .5, 1.5), r = 1.2, K = 1, sigma = 0.2,numyears = 100)
{
#create matrix for nrow=numyears, ncol=length(p0)
  N <- matrix(NA, numyears, length(p0))  #initialize empty matrix
  N[1, ] <- p0

  for (pop in 1:length(p0)) { #loop through the populations

    for (yr in 2:numyears){ #for each pop, loop through the years

      N[yr, pop] <- N[yr-1, pop] * exp(r * (1 - N[yr - 1, pop] / K) + rnorm(1, 0, sigma)) # add one fluctuation from normal distribution
    
     }
  
  }
  
 return(N)

}



# Now write another function called stochrickvect that vectorizes the above to
# the extent possible, with improved performance: 

stochrickForm <- function(p0, pop, numyears, r, K, sigma) {
  
  N <- rep(NA,numyears)
  N[1] <- p0[pop]

  for (yr in 2:numyears) {   
    N[yr] <- N[yr-1] * exp(r * (1 - N[yr-1] / K) + rnorm(1, 0, sigma))
  }
  return(N)
}

stochrickvect <- function(p0 = runif(1000, .5, 1.5), r = 1.2, K = 1, sigma = 0.2,numyears = 100) {

  result <- sapply(1:length(p0), function(pop) stochrickForm(p0,pop,numyears,r,K,sigma))
  
  return(result)
}

cat("\nIn R, the original vectorized Stochastic Ricker takes: \n")
cat(system.time(stochrick())[[3]],"\n")

cat("In R, the modified vectorized Stochastic Ricker takes: \n")
cat(system.time(stochrickvect())[[3]],"\n")