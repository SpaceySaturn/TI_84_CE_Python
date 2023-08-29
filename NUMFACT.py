#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 17:46:50 2023

@author: pi
"""

# Pythong program to compute factors of numbers

# Function computes the factor of argument

def print_factors(x):
    print("The factors of" ,x, "are:")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)
            
# Collects the number from the shell
numInput = input("Enter number: ")

# Converts the number into the an integer
num = int(numInput)

print_factors(num)