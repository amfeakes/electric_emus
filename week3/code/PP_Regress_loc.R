#!/usr/bin/env Rscript

#Author: Amy Feakes
#Script: PP_Regress.R
#Description: 
#Date: Oct 2022
#Clear workspace
rm(list=ls())

#Dependencies 
require(tidyverse)

#### importing data ####
df <- read.csv("../data/EcolArchives-E089-51-D1.csv")

#make factors 

df$Type.of.feeding.interaction <- factor(df$Type.of.feeding.interaction)
df$Location <- factor(df$Location)
df$Predator.lifestage <- factor(df$Predator.lifestage)
df$Predator.mass <- as.numeric(df$Predator.mass)

####converting all prey mass to g ####
#using mutate and case_when to create a new column for prey mass where all units are g 
df <- df %>%
  mutate(Prey.merge=case_when(
    Prey.mass.unit == "g" ~ Prey.mass,
    Prey.mass.unit == "mg" ~ Prey.mass/1000,
  ))

#### creating results ####


#set column names 
parameter_names <- c("Type.of.feeding.interaction", "Life.stage", "Location", "Intercept",
                     "Slope.Regression", "R.Squared", "F-statistic", "P-value")

#create matrix for parameters 
pp_results <- as.data.frame(matrix(NA, nrow=0, ncol=8))

#loop for each unique combination 
for (type in unique(df$Type.of.feeding.interaction)){
   type_par <- subset(df, df$Type.of.feeding.interaction == type)
   
  for(stage in unique(type_par$Predator.lifestage)){
     stage_par <- subset(type_par, type_par$Predator.lifestage == stage)
     
    for(loc in unique(stage_par$Location)){
      loc_par <- subset(stage_par, stage_par$Location == loc)

      if (nrow(loc_par) > 2) #only if data has more than 2 observations
        lin_results <- summary(lm(log10(loc_par$Predator.mass)~log10(loc_par$Prey.mass)))
        
      mod_results <- c(type, 
                       stage, 
                        loc,
                        round(lin_results$coefficients [[1]], 5), #intercept 
                        round(lin_results$coefficients [[2]], 5), #slope
                        round(lin_results$r.squared, 5),
                        round(lin_results$fstatistic [[1]], 5),
                        lin_results$coefficients[[2,4]])
                       # p value
      pp_results <- rbind(pp_results, mod_results) #make df
    }
  }
}
colnames(pp_results) <- parameter_names

# write.csv(pp_results , file = "../results/PP_Results_loc.csv")

str(pp_results)

