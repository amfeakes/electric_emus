#!/usr/bin/env Rscript

# Script: treeheight.R
# Author: Electric Emus (f.ferreira22@imperial.ac.uk, amy.feakes22@imperial.ac.uk, zitong.zhao22@imperial.ac.uk,
#                        xuanyin.zheng22@imperial.ac.uk, dongxuan.zhu22@imperial.ac.uk)
# Description: Practical work using functions 
# Date: Oct 2022

#Clear workspace
rm(list=ls())


###DESCRIPTION####
# csv format species name, distance, degrees 
# This function calculates heights of trees given distance of each tree 
# from its base and angle to its top, using  the trigonometric formula 
#
# height = distance * tan(radians)
#
# ARGUMENTS
# degrees: The angle of elevation of tree
# distance: The distance from base of tree (e.g., meters)

####CALCULATIONS####
# The heights of the tree, same units as "distance"
treeheight<- function(degrees, distance) {
    radians <- degrees * pi / 180
    height <- distance * tan(radians)
}

#### Command Line parameters#### 
# steps: input file, read file, create new colum tree height, calc tree heigh, create and put in new file 
main <- function () {
    args <- commandArgs(trailingOnly = TRUE) #this returns only arguments after 
    filename <- args[1] #inputing the file names in the command line 
    dat <- read.csv(file = filename) 
    dat$height.m <- NA #empty column
    dat[,4] <- treeheight(dat[,3], dat[,2])#this calculates tree height using above
    output_filename <- tools::file_path_sans_ext(basename(filename))
    output <- paste("../results/",output_filename,"_TreeHeights.csv", sep = "")
    write.csv(dat, output, row.names = FALSE)

    print("Completed Tree Height Calculation.")
    print("Data Files found in Results folder!!!")
}


main()

##issue - it doesnt work if in the command line you use a relative path to get to the data file 

