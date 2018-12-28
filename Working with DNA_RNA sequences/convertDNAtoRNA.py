#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 18:34:50 2018

@author: janicelove
"""
#open files
inFile = open ('readRNAseq.txt', 'r')
outFile = open ('convertedSeq.txt', 'w')

#read DNA sequence to variable dna 
dna = inFile.read()


#loop through file to convert DNA seq to RNA seq 
for i in dna:
    if i == "T":
        outFile.write ('U')
    else:
        outFile.write(i)

       
    