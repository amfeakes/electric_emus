#!/usr/bin/Rscript
# This script help answer the question: Are temperatures of one year
# significantly correlated with the next year, across years in a given location?
#### imports ####
rm(list=ls())
library(ggplot2)
load("../data/KeyWestAnnualMeanTemperature.RData")

#1 Compute the correlation coefficient between years and temperature
ats <- ats[order(ats$Year),]
tempNow <- ats$Temp[-(length(ats$Temp))]
tempNext <- ats$Temp[2:length(ats$Temp)]
cor1 <- cor(tempNow, tempNext, method =  c("pearson"))
#2 Recalculate correlation coeffient between temperature(random in order) and years
#permutation test
corTemps <- function(tempNow,tempNext) {

    temp_shuffle <- tempNow[sample(length(tempNow))]
    cor_shuffle <- cor(temp_shuffle,tempNext)
    
    return(cor_shuffle)
}

N <- 10000

corPerm <- sapply(1:N, function(i) corTemps(tempNow,tempNext))
corObserved <- cor(tempNow, tempNext)


png("../results/PermutationTest.png")
hist(corPerm, main = paste("Histogram of" , "Permutated Correlation Coefficient"), xlim=range(c(corPerm, corObserved)))
abline(v=corObserved, col="red")
dev.off()

#3 Calculate what fraction of the random correlation coefficients were greater than the observed one
#p-value
p_value_Cor <- (sum(abs(corPerm)>=abs(corObserved))+1)/length(corPerm)


