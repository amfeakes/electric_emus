#!/usr/bin/env ipython3

"""This script is used to find the best (and equally) best alignments for sequences. It uses inputs from the data directory, fasta files,
and outputs a text file in the results directory."""

__appname__ = 'align_seqs_better.py'
__author__ = 'Electric Emus (amy.feakes22@imperial.ac.uk, f.ferreira22@imperial.ac.uk,\
                             zitong.zhao22@imperial.ac.uk, xuanyin.zheng22@imperial.ac.uk,\
                             dongxuan.zhu22@imperial.ac.uk)'
__version__ = '0.0.1'

###IMPORTS###
import pickle #used to keep track of objects
import sys #reads in files from the user
from align_seqs_fasta import read_fasta, calculate_score, assign

###FUNCTIONS###

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

    
    print(f"\nOutputting best scores and alignments below.")
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
    print(f"\nCompleted!!!!\nFile with best alignment found is stored in Results Folder!!!")
    return 0

if __name__ == "__main__":
    status = main(sys.argv)
    sys.exit(status)
