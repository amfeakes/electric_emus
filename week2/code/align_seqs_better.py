#!/usr/bin/env python3

"""

"""

__appname__ = ['Align FASTA sequences']
__author__ = 'Vitor Ferreira (f.ferreira22@imperial.ac.uk)'


# Imports
import csv
import sys
import pickle

# create empty strings to store values
seq1 = ""
seq2 = ""

if len(sys.argv) == 3:

    # Read CSV files containing sequences
    with open(str(sys.argv[1]), 'r') as f1:

        f1 = f1.readlines()[1:]
        for line in f1:
            line = line.strip(r"\n")
            seq1 = seq1 + line

    with open(str(sys.argv[2]), 'r') as f2:

        f2 = f2.readlines()[1:]
        for line in f2:
            line = line.strip(r"\n")
            seq2 = seq2 + line

elif len(sys.argv) == 2:

    # Read CSV files containing sequences
    with open(str(sys.argv[1]), 'r') as f1:

        f1 = f1.readlines()[1:]
        for line in f1:
            line = line.strip(r"\n")
            seq1 = seq1 + line

    print("You only provide one FASTA file!!!")
    choice = input("Would you like to provide another sequence? y/n?")

    if choice == "y":
        dir_f2 = input("Please enter the file to sequence: ")

        with open(str(dir_f2), 'r') as f2:

            f2 = f2.readlines()[1:]
            for line in f2:
                line = line.strip(r"\n")
                seq2 = seq2 + line

    else:
        print("The default FASTA file will be provided "
              "to calculate sequencing score")

        with open("../data/fasta/407228412.fasta", 'r') as f2:

            f2 = f2.readlines()[1:]
            for line in f2:
                line = line.strip(r"\n")
                seq2 = seq2 + line

else:
    print("No FASTA files were provided!!! Defaults will be used!!!")

    # Read CSV files containing sequences
    with open("../data/fasta/407228326.fasta", 'r') as f1:

        f1 = f1.readlines()[1:]
        for line in f1:
            line = line.strip(r"\n")
            seq1 = seq1 + line

    with open("../data/fasta/407228412.fasta", 'r') as f2:

        f2 = f2.readlines()[1:]
        for line in f2:
            line = line.strip(r"\n")
            seq2 = seq2 + line


print("Looking for best alignment...")
print(".")
print(".")
print(".")

# Assign the longer sequence s1, and the shorter to s2
# l1 is length of the longest, l2 that of the shortest

l1 = len(seq1)
l2 = len(seq2)
if l1 >= l2:
    s1 = seq1
    s2 = seq2
else:
    s1 = seq2
    s2 = seq1
    l1, l2 = l2, l1  # swap the two lengths


# A function that computes a score by returning the number of matches starting
# from arbitrary startpoint (chosen by user)
def calculate_score( s1, s2, l1, l2, startpoint):
    """
    Computes a score by returning the number of matches starting
    from arbitrary startpoint (chosen by user)
    """
    matched = ""  # to hold string displaying alignments
    score = 0
    for i in range(l2):
        if (i + startpoint) < l1:
            if s1[i + startpoint] == s2[i]:  # if the bases match
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
my_best_align = []
my_best_score = -1

best_alignments_list = []
best_scores_list = []

for i in range(l1):  # Note that you just take the last alignment
    #                  with the highest score

    z = calculate_score(s1, s2, l1, l2, i)
    if z > my_best_score:
        my_best_score = z
        my_best_align = "." * i + s2
        best_alignments_list.append(my_best_align)
        best_scores_list.append(my_best_score)
    elif z == my_best_score:
        my_best_score = z
        my_best_align = "." * i + s2
        best_alignments_list.append(my_best_align)
        best_scores_list.append(my_best_score)

best_alignments_list.reverse()
best_scores_list.reverse()

combined = []
for i in range(len(best_scores_list)):
    combined.append([best_scores_list[i], best_alignments_list[i]])


# with open('../results/align_seqs_output_better.csv', 'w') as o:
#
#     csvwrite = csv.writer(o)
#     csvwrite.writerow([f"The best scores and alignments are: {combined}"])

# Writing files to binary python object
f_pckl = open('../results/align_seqs_better_bin_output.p', 'wb')
pickle.dump(combined, f_pckl)
f_pckl.close()


print("Done!!!")
print("Best alignment scored!")
print("Output file can be found in results folder!!!")
