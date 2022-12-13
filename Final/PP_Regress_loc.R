#!/usr/bin/env Rscript

# Script: PP_Regress_loc.R
# Author: Electric Emus (dongxuan.zhu22@imperial.ac.uk, f.ferreira22@imperial.ac.uk, 
#                        amy.feakes22@imperial.ac.uk, zitong.zhao22@imperial.ac.uk,
#                        xuanyin.zheng22@imperial.ac.uk)
# Description: Practical work using functions 
# Date: Oct 2022

# Clear workspace
rm(list=ls())

# Load data
MyDF <- read.csv("../data/EcolArchives-E089-51-D1.csv")

## Functions ##
reg <- function(SubData,k){

    if (nrow(SubData[SubData$Location == catLocation[k], ]) == 0) { 
        return (rep(NA,8))
        }
   
    M <- rep(NA,8)

    MyLM <- summary(lm(log(Predator.mass) ~ log(Prey.mass), data = SubData[SubData$Location == catLocation[k], ]))
    
    if (length(MyLM$fstatistic) == 0) {MyLM$fstatistic = NA}#how to improve this part
    M[1] <- MyLM$coefficients[[1]]
    M[2] <- MyLM$coefficients[[2]]
    M[3] <- MyLM$r.squared[[1]]
    M[4] <- MyLM$fstatistic[[1]]
    M[5] <- MyLM$coefficients[[1,4]] #[2,4] out of range?
    M[6] <- catLifestage[[i]]
    M[7] <- catType[[j]]
    M[8] <- catLocation[[k]]

    return(M)
}

print("Running regression analysis on Predator-Prey mass ratios from Ecological Archives - ESA")
print(".")
print(".")
print(".")

## data wrangling ##
# MyDF$Type.of.feeding.interaction <- as.factor(MyDF$Type.of.feeding.interaction)
# MyDF$Location <- as.factor(MyDF$Location)
regDF <- as.data.frame(MyDF[,c("Type.of.feeding.interaction","Prey.mass","Predator.mass","Predator.lifestage","Location")],stringsAsFactors = F)



## linear regression ##

catType <- as.character(unique(regDF$Type.of.feeding.interaction))
numType <- length(catType)
catLifestage <- as.character(unique(regDF$Predator.lifestage))
numLifestage <- length(catLifestage)
catLocation <- as.character(unique(regDF$Location))
numLocation <- length(catLocation)

# rowDF <- numType*numLifestage*numLocation
outDF <- data.frame(matrix(NA,0,8))

suppressWarnings(
for (i in 1:numLifestage){
   
    for (j in 1:numType){
     
        if (nrow(regDF[regDF$Type.of.feeding.interaction == catType[j] 
                            & regDF$Predator.lifestage == catLifestage[i], ]) == 0) {
                                next
                            }

        SubData = regDF[regDF$Type.of.feeding.interaction == catType[j] 
                            & regDF$Predator.lifestage == catLifestage[i], ]
        
        locDF = t(sapply(1:numLocation, function(k) reg(SubData,k)))
        outDF <- rbind(outDF,locDF)
        # browser()
        
    }
})

outDF <- outDF[complete.cases(outDF),]

colnames(outDF) <- c("intercept","slope","r.squared","fstatistic","p.value","Predator.lifestage","Type.of.feeding.interaction","Location")

# ## exports ##
write.csv(outDF, "../results/PP_Regress_loc_Results.csv",row.names=FALSE)
print("Analysis completed. Output can be found in the Results folder!!!")

