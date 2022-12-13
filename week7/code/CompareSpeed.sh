#!/bin/sh
# Author: Dongxuan Zhu dongxuan.zhu22@imperial.ac.uk
# Script: CompareSpeed.sh
# Desc: Compare execution speed for four vectorization scripts inc. detailed functions.
# Arguments: none
# Date: Dec 2022

echo "\nSummary:"
echo "\nThe Vectorize1.py script takes:"
time python3 Vectorize1.py > ../results/CompareVect.txt 
echo "\nThe Vectorize1.R script takes:"
time Rscript Vectorize1.R  >> ../results/CompareVect.txt 
python3 Vectorize1.py
Rscript Vectorize1.R
echo "\nThe Vectorize2.py script takes:"
time python3 Vectorize2.py >> ../results/CompareVect.txt 
echo "\nThe Vectorize2.R script takes:"
time Rscript Vectorize2.R >> ../results/CompareVect.txt 
python3 Vectorize2.py 
Rscript Vectorize2.R 

