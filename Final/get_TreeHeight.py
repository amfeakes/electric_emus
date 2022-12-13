#!/usr/bin/env python3

"""
    This function calculates heights of trees given distance of each tree 
    from its base and angle to its top, using  the trigonometric formula
"""

__appname__ = 'get_TreeHeight.py'
__author__ = 'Electric Emus (amy.feakes22@imperial.ac.uk, f.ferreira22@imperial.ac.uk,\
                             zitong.zhao22@imperial.ac.uk, xuanyin.zheng22@imperial.ac.uk,\
                             dongxuan.zhu22@imperial.ac.uk)'
__version__ = '0.0.1'

#Imports
import sys
import pandas as pd
import numpy as np


# Functions
def treeheight(degrees, distance):
    """ Calculates the height of the trees"""
    radians = np.radians(degrees)
    height = distance * np.tan(radians)
    return height

def main(argv):
    """Main function to call the script"""
    file=sys.argv[1]
    filename=file.split(".")[0]
    df=pd.read_csv(file)
    df["Tree.Height.m"]=treeheight(df["Angle.degrees"],df["Distance.m"])
    filename=file.split("/")[-1]
    filename=filename.split(".")[0]
    outpath=(f"../results/{filename}_TreeHeights_py.csv")
    df.to_csv(outpath,index=False)
    
print(f"\nCompleted Tree Height Calculation.\nData Files found in Results folder!!!")

    
if (__name__ == "__main__"):
    status = main(sys.argv)
    sys.exit(status)
