#!/bin/bash
# Author: Dongxuan Zhu dongxuan.zhu22@imperial.ac.uk
# Script: CompileLaTex.sh
# Description: Compile reference list and render LaTex document properly in pdf format.
#
# Arguments: 1 -> user input LaTex document
# Date: Oct 2022

[ -z "$1" ] && echo "Please specify a LaTex document." && exit
pdflatex -halt-on-error -output-directory ../writeup ../writeup/$(basename -s .tex "$1")
pdflatex $1
bibtex $(basename -s .tex "$1")
pdflatex $1
pdflatex $1
evince ../writeup/$(basename -s .tex "$1").pdf &

##Cleanup
rm *.aux
rm *.log
rm *.bbl
rm *.blg

