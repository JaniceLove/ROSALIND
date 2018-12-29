#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 19:11:32 2018

@author: janicelove
"""
#required for float division python 2
from __future__ import division
#open files
inFile = open ('GCcontentFASTAfile.txt', 'r')
outFile = open('GCcalculated.txt', 'w')
tempFile = open('temp.txt', 'w')


#function to calculate GC content 
def calcGC (seq):
    total_count = len(seq)
    gc = seq.count('G') + seq.count('C')
    gc_content = (gc / total_count)*100
    return gc_content

for line in inFile:
    if ">" in line:
        tempFile.write(line)
    else:
        line = line.rstrip('\n')
        tempFile.write(line)

tempFile.close()
tempFile = open('temp.txt', 'r')


#loop through FASTA file
for line in tempFile:
    if ">" in line:
        temp = line 
        outFile.write(temp)
    else:
        x = calcGC(line)
        print ('temp line is:'), temp, (x)