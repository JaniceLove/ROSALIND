#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 18:54:26 2018

@author: janicelove
"""

inFile = open('seq_to_revComp.txt', 'r')
outFile = open('reversedSequence.txt', 'w')

seq = inFile.read()
seq_reversed = seq[::-1]

for i in seq_reversed:
    if i == "A":
        outFile.write("T")
    elif i == "T":
        outFile.write('A')
    elif i == "C":
        outFile.write("G")
    elif i == "G":
        outFile.write ("C")

inFile.close()
outFile.close()
