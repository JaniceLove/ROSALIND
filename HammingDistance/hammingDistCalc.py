#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 12:42:24 2018

@author: janicelove
"""
from itertools import izip 
f = open('sequenceFile.txt', 'r')
seq = f.read()
seq1 = seq.split()

list1 = seq1[0]
list2 = seq1[1]

#check length is equal
if len(list1) == len(list2):
    print ('sequence lengths are equal:' ), len(list1)
        
def hamDist(a,b):
    #calculate # of differences between the two strings (as lists)
    diff = 0
    for char1, char2 in zip(a,b):
        if char1 != char2:
            diff = diff + 1
    return diff 

dist = hamDist(list1, list2)
print ('number of differences: '), dist









#f.close()