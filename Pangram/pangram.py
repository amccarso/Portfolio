#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 13:29:21 2018

@author: austinmccarson
"""



def pangram(inputx, output):
    # read input file line by line
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    found = ""
    
    # for every line in input file, check if it contains all alphabets
    file = open(inputx, "r")
    out = open(output, "w+")

    lines = file.readlines()

    for line in lines:
        for char in line:
            if char in alphabet and char not in found:
                found += char
            
        out.write('true \n') if len(found) == 26 else out.write('false \n')
        found = ""

    file.close()
    out.close()
    # store result (true/false) in a variable
    # write result to output file
