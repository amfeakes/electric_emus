#!/usr/bin/env ipython3

"""This script is used to find the best (and equally) best alignments for sequences. It uses inputs from the data directory, fasta files,
and outputs a text file in the results directory."""

__appname__ = 'align_seqs_better.py'
__author__ = 'Amy Feakes (amf222@ic.ac.uk)'
__version__ = '0.0.1'

###IMPORTS###
import pickle #used to keep track of objects
import sys #reads in files from the user
#import os
###FUNCTIONS###

#######################
#this function reads in the fasta from the data directory
#strips the additional line from the file
#returns two objects - seqa and seqb

def read_fasta(fx):
    """This opens the fasta file and strips it to just the sequence."""
    with open(fx, 'r') as file:
        fasta = ""
        line = 0 #looking at the first line
        for row in file:
            if line != 0:
                fasta += row.replace("\n","") #empyting line and replacing it
            line += 1
    return fasta #returing the stripped sequence

##########################
#this function computes the score of the alignment
#using a for loop and the length of the sequences
def calculate_score(s1, s2, l1, l2, startpoint):
    """This computes the score."""
    matched = "" # to hold string displaying alignements
    score = 0
    for i in range(l2):
        if (i + startpoint) < l1:
            if s1[i + startpoint] == s2[i]: # if the bases match
                matched = matched + "*"
                score = score + 1
            else:
                matched = matched + "-"
    # some formatted output
    #print("." * startpoint + matched)
    #print("." * startpoint + s2)
    #print(s1)
    #print(score)
    #print(" ")

    return score
#############################
#this function takes the inputted sequences, calaculates their length
#it requires the first seqeneces to be longer than the second - if this is not already the case this will swap the sequences around
def assign(foo1: object, foo2: object) -> object:
    """"This function assiengs the longer sequence to seq1 and the shorter to seq2."""
    #os.rename(seq1, s1)
    #os.rename(seq2, s2)
    l1 = len(foo1)
    l2 = len(foo2)
    if l1 < l2:  # if l1 is less than l2, swap them around
        foo1, foo2 = foo2, foo1  # swap the two seqeuns
        l1, l2 = l2, l1  # swap the two lengths
    #print(foo1)
# now try to find the best match (highest score) for the two sequences
    return foo1, foo2, l1, l2

##############################
#this function calculates the best score and best alignment
#this function uses calculate_score function (already defined)
#uses a for loop with a range of the length of seq1
def calculate_best(s1, s2, l1, l2):
    """This finds the best match for the fasta sequences."""
    best_a = None
    best_s = -1
    best_all = {} #creating dic for all best alignments

#the dictionary uses key and value pairs
    for i in range(l1): # Note that you just take the last alignment with the highest score
        z = calculate_score(s1, s2, l1, l2, i)

        if z > best_s: #clearing matches cuase found new best score
            best_all = {}

            best_a = "." * i + s2 # think about what this is doing!
            best_s = z

            best_all["Align " + str(1)]=[best_s, best_a]

        elif z == best_s:
            best_a = "." * i + s2  # think about what this is doing!
            value = len(best_all.keys())
            best_all["Align " + str(value + 1)]=[best_s, best_a]
    return best_all, best_s

#print(best_a)
#print(s1)
#print("Best score:", best_s)

# Test the function with some example starting points: just to understnad, will not be in final script
# calculate_score(s1, s2, l1, l2, 0)
# calculate_score(s1, s2, l1, l2, 1)
# calculate_score(s1, s2, l1, l2, 5)

###STANDARD FUNCTIONS###
def main(argv):
    """Read in the data from fasta files, find the best algiment and save the results."""
    if len(sys.argv) <= 2:
        print("Not enough arugments were inputted, script will be run with the default sequences")
    #input the defult sequences
        fasta1=read_fasta("../data/407228326.fasta")
        fasta2=read_fasta("../data/407228412.fasta")
    else: #when arguements inputted
        print("Reading inputted files")
        fasta1 = read_fasta(argv[1])
        fasta2 = read_fasta(argv[2])
    #assigning seq
    s1, s2, l1, l2 = assign(fasta1, fasta2)
    #calculations
    best_all, best_s = calculate_best(s1, s2, l1, l2)

    print("Outputting best scores and alignments below.")
    for key, value in best_all.items():
        print(key, ": ", value[0], ", ", value[1], sep="")
    print
    #dump the dictionary of best_all into a file
    pickle_out = open("../data/align_seqs_better.pickle", "wb")
    pickle.dump(best_s, pickle_out)
    pickle_out.close()
    #output
    with open('../results/align_seqs_better_results.txt', 'w') as x:
        for key, value in best_all.items():
            x.write("Best alignmment: " + value[1] + "\n" + "Best score: " + str(value[0]) + "\n")
    return 0

if __name__ == "__main__":
    status = main(sys.argv)
    sys.exit(status)