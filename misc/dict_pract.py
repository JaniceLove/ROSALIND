#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 12:05:56 2018

@author: janicelove
"""

#for word in str.split(' '):
#    print word

dict = {}

f = open ("output.txt", 'r')

for word in f:
    word = word.split(' ')
    for item in word:
        dict[item] =  word.count(item)

    
for key, value in dict.items():
    print key, value
'''
dict([word.split() for word in f])


def word_count(word):
  my_string = string.lower().split()
  my_dict = {}
  for item in my_string:
    my_dict[item] = my_string.count(item)
  print(my_dict)

word_count("I am that I am.")
'''