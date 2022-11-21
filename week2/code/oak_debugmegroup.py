# 修改脚本，使其在给定数据集中搜索橡树
# 时排除标题行（如果存在）。
# 您可能还注意到程序的输出写入了一个仅包含橡树名称的新文件。
# 但是，它不包括列标题（“属”、“种”）。解决这个问题。

""" This script modifies the previous script to focus on searching for oak trees and solves a problem with a new file containing only the name, is a groupwork"""
__appname__ = 'oaks_debugmegroup.py'
__author__ = 'Xuanyin Zheng (xz1322@ic.ac.uk)'
__version__ = '0.0.1'

import csv
import sys
import doctest

#Define function
def is_an_oak(name):
    """ Returns True if name is starts with 'quercus' 
    >>> is_an_oak("Quercus")
    True
    >>> is_an_oak("Genus")
    False
    >>> is_an_oak("Fraxinus")
    False
    >>> is_an_oak("Pinus")
    False
    >>> is_an_oak("Quercuss")
    False
    >>> is_an_oak("Quercussquercus")
    False
    >>> is_an_oak("quercus")
    True
    >>> is_an_oak("quercusquercus")
    False
    """
    return name.lower().startswith('quercus')
doctest.testmod()

def main(argv): 
    f = open('../data/TestOaksData.csv','r')
    g = open('../results/JustOaksData.csv','w')
    taxa = csv.reader(f)
    next(taxa, None)
    csvwrite = csv.writer(g)
    oaks = set()
    csvwrite.writerow(["Genus", "species"])
    
    for row in taxa:
        print(row)
        print ("The genus is: ") 
        print(row[0] + '\n')
        if is_an_oak(row[0]):
            print('FOUND AN OAK!\n')
            csvwrite.writerow([row[0], row[1]])    

    return 0
    
if (__name__ == "__main__"):
    status = main(sys.argv)