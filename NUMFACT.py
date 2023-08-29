#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: pi
"""

# Python program to compute factors of numbers

# Function computes the factor of argument

def print_factors(x):
    print("The factors of" ,x, "are:")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)
 
# Asks for user input        
while True:
    numInput = input("Enter number here: ")
    # Quits the program if the input is quit
    if numInput == "quit":
        break
    else:
        num = int(numInput)
        print_factors(num)
