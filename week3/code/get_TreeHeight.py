#!/usr/bin/env python3

"""This script is a python version of get_TreeHeight.R, which parse input file name and return the calculated tree \
height with customized output file name."""

_appname_ = 'get_treeheight'
_author_ = 'Dongxuan Zhu (dongxuan.zhu22@imperial.ac.uk)'
_version_ = '0.0.1'
_license_ = "N/A"

#### imports ####
import sys
from math import pi, tan
import pandas as pd
from pathlib import Path


#### functions ####
def treeheight(degrees, distance):
    """Calculate tree height based on the angle of elevation\
    and distance from the base from the tree. Returns with the same unit as distance."""
    radians = degrees * pi / 180
    height = distance * tan(radians)
    return height

def main(argv):
    """Parse filename and execute tree height calculation."""
    if len(argv) == 2:
        filename = argv[1]
        tree_data = pd.read_csv(filename)
        tree_deg = tree_data["Angle.degrees"].astype(float)
        tree_dis = tree_data["Distance.m"].astype(float)
        tree_data["Height.m"] = [treeheight(deg,dis) for deg,dis in zip(tree_deg,tree_dis)]
        #export
        filename_output = f"../results/{Path(filename).stem}_treeheights.csv"
        tree_data.to_csv(filename_output,index=False)
        print("Tree height data saved as "+filename_output)
    else:
        print("Please specify one csv file with tree measurement data (degrees,distance).")

    
#### execution ####
if (__name__ == "__main__"):
    status = main(sys.argv)
    sys.exit(status)
