#!/usr/bin/Rscript

## imports ##
rm(list=ls())
load("../data/KeyWestAnnualMeanTemperature.RData")

## process ##
#1 Compute the correlation coefficient between years and temperature

cor1 <- cor(ats$Temp, ats$Year, method =  c("pearson", "kendall", "spearman"))

#2 Recalculate correlation coeffient between temperature(random in order) and years
#permutation test
corTempYear <- function(temp,year) {

    temp_shuffle <- temp[sample(length(temp))]
    cor_shuffle <- cor(temp_shuffle,year)
    
    return(cor_shuffle)
}

N <- 10000

corPerm <- sapply(1:N, function(i) corTempYear(ats$Temp,ats$Year))
corObserved <- cor(ats$Temp, ats$Year)


# png("../data/PermutationTest.png")
# hist(corPerm, main = paste("Histogram of" , "Permutated Correlation Coefficient"), xlim=range(c(corPerm, corObserved)))
# abline(v=corObserved, col="red")
# dev.off()


#3 Calculate what fraction of the random correlation coefficients were greater than the observed one
#p-value
p_value_Cor <- (sum(corPerm>=corObserved)+1)/length(corPerm)


