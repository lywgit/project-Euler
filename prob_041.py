#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 18:38:44 2017

@author: lywang

Problem 41 Pandigital prime

"""

from prob_010 import is_prime
from prob_032 import permutation_generator, digits_to_int

def largest_pandigital_prime(verbose = False):
    digits = '987654321'
    found = False
    largest = 0;
    while len(digits)>0 and not found:
        if verbose:
            print("searching permutation of: ", digits)
        gen = permutation_generator(list(digits))
        for sequence in gen:
            i = digits_to_int(sequence)
            #print(i)
            if is_prime(i):
                found = True
                largest = i;
                if verbose:
                    print("Found: ", largest)
                break
        digits = digits[1:]
    return largest

if __name__ == '__main__':
    largest = largest_pandigital_prime(verbose = True)


