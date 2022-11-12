#!/usr/bin/env python3

"""Practice on control flow tools."""

_appname_ = 'DNA alignment for fasta files'
_author_ = 'Dongxuan Zhu (dongxuan.zhu22@imperial.ac.uk)'
_version_ = '0.0.2'
_license_ = "N/A"

## imports ##
# Import DNA sequence from external files

import csv
import sys
import numpy as np

default_seq1 = "../data/407228326.fasta"
default_seq2 = "../data/407228412.fasta"
seq1 = ""
seq2 = ""

if len(sys.argv) <= 2:
    input_seq1 = default_seq1
    input_seq2 = default_seq2
    print("Input source directory not specified, using default file:\n" + \
     str(default_seq1)+" and " + str(default_seq2))
else:
    input_seq1 = sys.argv[1]
    input_seq2 = sys.argv[2]

with open(input_seq1,'r') as f1:
    next(f1)
    for line in f1:
        seq1 = seq1 + str(line)
with open(input_seq2,'r') as f2:
    next(f2)
    for line in f2:
        seq2 = seq2 + str(line)


## preprocession ##
# Assign the longer sequence s1, and the shorter to s2
# l1 is length of the longest, l2 that of the shortest

# Retrieve length of sequences
l1 = len(seq1)
l2 = len(seq2)

if l1 >= l2:
    s1 = seq1
    s2 = seq2
else:
    s1 = seq2
    s2 = seq1
    l1, l2 = l2, l1 # swap the two lengths

## functions ##
# A function that computes a score by returning the number of matches starting
# from arbitrary startpoint (chosen by user)
def calculate_score(s1, s2, l1, l2, startpoint):

    """Find best alignment score by counting how many DNA sequences match after the starting point."""
    matched = "" # to hold string displaying alignements
    score = 0
    for i in range(l2):
        if (i + startpoint) < l1: #why not l2: the aim is to move s1 and get the most fit-in section.
            if s1[i + startpoint] == s2[i]: # if the bases match
                matched = matched + "*"
                score = score + 1
            else:
                matched = matched + "-"

    # some formatted output
    # print("." * startpoint + matched)           
    # print("." * startpoint + s2)
    # print(s1)
    # print(score) 
    # print(" ")

    return score

# Test the function with some example starting points:
# calculate_score(s1, s2, l1, l2, 0)
# calculate_score(s1, s2, l1, l2, 1)
# calculate_score(s1, s2, l1, l2, 5)

# now try to find the best match (highest score) for the two sequences
my_best_align = None
my_best_score = -1

for i in range(l1): # Note that you just take the last alignment with the highest score

    z = calculate_score(s1, s2, l1, l2, i)
    if z > my_best_score:
        my_best_align = "." * i + s2 #It shows till what starting point starts the best alignment.
        my_best_score = z 
    elif z == my_best_score:
        my_best_align = np.append(my_best_align,("."*i + s2))

# print("Best alignment: ", my_best_align)
# print("Best score: ", my_best_score)

## output ##
if len(my_best_align[1]) > 1: #if there are more than one equally best alignment, the output will be separated with \n
    align_seqs_output = ["Best alignment: ", '\n'.join(my_best_align), \
    "Best score: " + str(my_best_score)]
else:                         #if there's only one best alignment, print out as it is.
    align_seqs_output = ["Best alignment: ", my_best_align, \
    "Best score: " + str(my_best_score)]


out_file = "../results/align_seqs_better_output.txt"
with open(out_file,'w') as g:
    
    for i in align_seqs_output:
        g.write(i + "\n")

    print("Done! Best alignment stored as: " + str(out_file))




    

