#!/usr/bin/env python3

"""save the tree height"""

__appname__ = 'get_TreeHeight.py'
__author__ = 'Zitong Zhao (zitong.zhao22@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program"

import sys
import pandas as pd
import numpy as np



def treeheight(degrees, distance):
    radians = np.radians(degrees)
    height = distance * np.tan(radians)
    return height

def main(argv):
    file=sys.argv[1]
    filename=file.split(".")[0]
    df=pd.read_csv(file)
    df["Tree.Height.m"]=treeheight(df["Angle.degrees"],df["Distance.m"])
    filename=file.split("/")[-1]
    filename=filename.split(".")[0]
    outpath=(f"../results/{filename}_TreeHeights_py.csv")
    df.to_csv(outpath,index=False)

    
if (__name__ == "__main__"):
    status = main(sys.argv)
    sys.exit(status)
