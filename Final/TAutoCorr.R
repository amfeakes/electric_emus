#!usr/bin/env Rscript

##------------------------------------------
## Name: TAutoCorr.R
## Description: Script that analyses a potential serial autocorrelation in 
##              Key West, Florida
## Author: Electric Emus (f.ferreira22@imperial.ac.uk, amy.feakes22@imperial.ac.uk, zitong.zhao22@imperial.ac.uk,
##                        xuanyin.zheng22@imperial.ac.uk, dongxuan.zhu22@imperial.ac.uk)
## Date: December 2022
##------------------------------------------


# Clean enviroment
rm(list = ls())

# Clear graphics
graphics.off()

# Load libraries
suppressMessages(require(tidyverse, quietly = T))

# Loading data
load("../data/KeyWestAnnualMeanTemperature.RData")


#########################################################################
# PRACTICAL QUESTION
# Are the Temperatures of one year significantly correlated with the
# next year (Successive years), across years in given location?
#########################################################################


##### Data Preparation #####
# PROCEDURES EXPLANATION:
# First we create two vectors with the temperature values.
# On the temp0 vector we remove the last year (2000)
# And on the temp1 we remove the first year (1901)
# We assign the vectors into a data frame and
# calculate the initial correlation coefficient
temp0 <- head(ats$Temp, length(ats$Temp) - 1)
temp1 <- tail(ats$Temp, length(ats$Temp) - 1)
df <- data.frame(temp0, temp1)

png("../results/Florida_Temperatures_relationship.png")
plot(df$temp0, df$temp1,
     main = "Annual Temperature Relationship \n(time-series (n-1))",
     xlab = "t0",
     ylab = "t1")
abline(lm(df$temp1 ~ df$temp0), col = "red", lty = 3, lwd = 3)

Sys.sleep(0.1)
graphics.off()

# Calculate the Initial Correlation
initial_cor <- cor(df$temp0, df$temp1)



##### Simulations #####
# For the simulation we create a function that calculates the
# autocorrelation coefficient. We create a sample of the temperatures and
# feed it into the function to generate and populate the autocorrelation vector

# Function to calculate the autocorrelation value between years
find_autocorr <- function(v){
  temp0 <- head(v, length(v)-1)
  temp1 <- tail(v, length(v)-1)

  corfit <- cor(temp0, temp1)

  return(corfit)
}


# Setting the simulation parameters
n_iters <- 10000
temp_cor <- vector( , n_iters)

for (i in 1:n_iters){
  temp_cor[i] <- find_autocorr(sample(ats$Temp, replace = FALSE))
}

png("../results/Florida_Temperatures_cor_density.png")
plot(density(temp_cor), 
     main = "Correlation Coefficients of Randomized temperature\n(time series (1900-2000))",
     col = "red",
     xlab = "Correlation coefficients")
abline(v = initial_cor, col = "blue", lty = 3, lwd = 3)
text(x = (initial_cor-0.075), y = 3, 
     labels = paste("Initial\nCorrelation\nr = ", round(initial_cor, 3)),
     col = "blue", cex = 1)

Sys.sleep(0.1)
graphics.off()

# The p-value it is calculated as a fraction of correlation coefficients 
# greater that initial correlation
autocor_ratio <- (sum(temp_cor > initial_cor)) / n_iters

