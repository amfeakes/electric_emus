#!/bin/bash
# Author: Zitong Zhao zitong.zhao22@imperial.ac.uk
# Script: run_get_TreeHeight
# Description: run the tree file and gain the tree height file
#
# Arguments: into space separated values file
# Date: Dec 2022


#run the R script
file =../results/trees_treeheights.csv
if [ $# -eq 1 ] ; then
  Rscript get_TreeHeight.R $1
  if [ -f "$file"]; then
    echo "R script -- using file $1 and output file $file"
  else
    echo "R script can not run sucessfully"
    exit 1
  fi
  
else
  Rscript get_TreeHeight.R ../data/trees.csv
  if [ -f "$file"]; then
    echo "R script -- using file trees.csv and output file $file"
  else
    echo "R script can not run sucessfully"
    exit 1
  fi
fi

#run the python script
if [ $# -eq 1 ] ; then
  python3 get_TreeHeight.py $1
  if [ -f "$file"]; then
    echo "python3 -- using file $1 and output file $file"
  else
    echo "python3 can not run sucessfully"
    exit 1
  fi
  
else
  python3 get_TreeHeight.R ../data/trees.csv
  if [ -f "$file"]; then
    echo "python3 -- using file trees.csv and output file $file"
  else
    echo "python3 can not run sucessfully"
    exit 1
  fi
fi
