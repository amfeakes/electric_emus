#!/usr/bin/Rscript


## imports ##
rm(list=ls())

# require(tidyverse)
# tidyverse_packages(include_self = TRUE)


MyDF <- read.csv("../data/EcolArchives-E089-51-D1.csv")

## functions ##
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


# test <- function() {
#     return( matrix(NA,8,1))
# }

# M <- t(sapply(1:25, function(i) test()))



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
}
outDF <- outDF[complete.cases(outDF),]
outDF
colnames(outDF) <- c("intercept","slope","r.squared","fstatistic","p.value","Predator.lifestage","Type.of.feeding.interaction","Location")

# ## exports ##
write.csv(outDF, "../results/PP_Regress_loc_Results.csv",row.names=FALSE)
print("Script completed. Please check the output at ../results/PP_Regress_loc_Results.csv")

