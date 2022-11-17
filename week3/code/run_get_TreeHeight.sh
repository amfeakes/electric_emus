#!/bin/bash

#Author: Amy Feakes amy.feakes222@imperial.ac.uk
#Script: run_get_TreeHeight.sh
#Desc: UNIX shell script to test get_TreeHeight.R and .py
#Date: Nov 2022

##Instructions 
##Write a Unix shell script called run_get_TreeHeight.sh that tests get_TreeHeight.R. 
##Include trees.csv as your example file. Note that source will not work in this case as 
##it does not allow scripts with arguments to be run; you will have to use Rscriptinstead.


#defult file 
TREEFILE='../data/trees.csv'

#check to see if file is inputted, if not continue with default 
if [ $# -eq 1  ]; then   
    echo "Running get_TreeHeight.R with the user file $1"
    Rscript get_TreeHeight.R $1
    echo "Now checking to see if the output has been made"
    #checking for file in results 
    #####Change trees to $1/basename
    if [ -e ../results/trees_TreeHeights.csv ]
    then 
    echo "R script ran and file was sucessfully outputted"
    rm ../results/trees_TreeHeights.csv
    else 
    echo "R script was unsucessful, output file was not created"
    fi

else 
    echo "Running get_TreeHeight, R with the default file"
    Rscript get_TreeHeight.R ${TREEFILE}
    echo "Now checking to see if the output has been made"
    #checking for file in results 
    RES="../results/trees_TreeHeights.csv"
    if [ -f $RES ]
    then 
    echo "R script ran and file was sucessfully outputted"
    rm ../results/trees_TreeHeights.csv
    else 
    echo "R script was unsucessful, output file was not created"
    fi

fi

##Run with python script 
#check to see if file is inputted, if not continue with default 
if [ $# -eq 1  ]; then   
    echo "Running get_TreeHeight.R with the user file $1"
    ipython3 get_TreeHeight.py $1
    echo "Now checking to see if the output has been made"
    #checking for file in results 
    #####Change trees to $1/basename
    if [ -e ../results/trees_TreeHeights.csv ]
    then 
    echo "R script ran and file was sucessfully outputted"
    rm ../results/trees_TreeHeights.csv
    else 
    echo "R script was unsucessful, output file was not created"
    fi

else 
    echo "Running get_TreeHeight, R with the default file"
    ipython3 get_TreeHeight.py $f
    echo "Now checking to see if the output has been made"
    #checking for file in results 
    RES="../results/trees_TreeHeights.csv"
    if [ -f $RES ]
    then 
    echo "R script ran and file was sucessfully outputted"
    else
    echo "R script was unsucessful, output file was not created"
    fi

fi