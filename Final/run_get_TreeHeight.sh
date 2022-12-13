#!/bin/bash

# Script: run_get_TreeHeight
# Author: 'Electric Emus (zitong.zhao22@imperial.ac.uk, amy.feakes22@imperial.ac.uk, 
#                         f.ferreira22@imperial.ac.uk, xuanyin.zheng22@imperial.ac.uk,
#                         dongxuan.zhu22@imperial.ac.uk)'
# Description: run the tree file and gain the tree height file
# Arguments: into space separated values file
# Date: Dec 2022


#run the R script
TREEFILE='../data/trees.csv'

if [ $# -eq 1 ] ; then
  Rscript get_TreeHeight.R $1
  Routput=../results/trees_TreeHeights.csv
  if [ -f "$Routput" ]; then
    echo "R script -- using file $1 and output file $Routput"
  else
    echo "R script can not run sucessfully"
    exit 1
  fi
  
else
  Rscript get_TreeHeight.R $TREEFILE
  Routput=../results/trees_TreeHeights.csv
  if [ -f "$Routput" ]; then
    echo "R script -- using file trees.csv and output file $Routput"
  else
    echo "R script can not run sucessfully"
    exit 1
  fi
fi



#run the python script
if [ $# -eq 1 ] ; then
  python3 get_TreeHeight.py $1
  Poutput=../results/trees_TreeHeights_py.csv
  if [ -f "$Poutput" ]; then
    echo "python3 -- using file $1 and output file $Poutput"
  else
    echo "python3 can not run sucessfully"
    exit 1
  fi
  
else
  python3 get_TreeHeight.py ${TREEFILE}
  Poutput=../results/trees_TreeHeights_py.csv
  if [ -f "$Poutput" ]; then
    echo "python3 -- using file trees.csv and output file $Poutput"
  else
    echo "python3 can not run sucessfully"
    exit 1
  fi
fi
