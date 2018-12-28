#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 17:54:00 2018

@author: janicelove
"""
#open sequence file and read to variable
inFile = open ('readDNAseq.txt', 'r')
dna = inFile.read()

#print dna string provided
print ('DNA string:'), dna

#count each nucleotide accurance and print 
a = dna.count('A')
t = dna.count('T')
g = dna.count('G')
c = dna.count('C')

print ('number of A:') , a
print ('number of T:') , t
print ('number of G:') , g
print ('number of C:') , c
   
print a,c,g,t           
        
#NOTE: it would be better use if else to iterate through file once instead of 4 times    