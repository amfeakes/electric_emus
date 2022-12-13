#!/bin/bash
# Author: Xuanyin Zheng(xz1322@ic.ac.uk)
# Script: runvectorize.sh
# Desc: Compare speed of functionsWhether with vectorization in R and python
# Arguments: none
# Date: 2022. Nov


echo -e "\nSummary:"
echo -e "\n the run time in Vectorize1.py is:"
time python Vectorize1.py
echo -e "\n the run time in Vectorize1.R is:"
time Rscript Vectorize2.R

echo -e "\n the run time in Vectorize2.py is:"
time python Vectorize2.py
echo -e "\n the run time in Vectorize2.R is:"
time Rscript Vectorize2.R


#exit
