#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 11:42:07 2017

@author: lywang

Problem 36 Double-base palindromes
"""


def sum_palindrome_base_2_and_10(limit):
    """
    limit: integer
    """
    summation = 0
    for i in range(limit):
        if is_palindrome_base_2_and_10(i):
            #print(i, bin(i))
            summation += i  
    return summation

def is_palindrome_base_2_and_10(n):
    """
    n: integer 
    """
    return is_palindrome(str(n)) and is_palindrome(bin(n)[2:]) 


def is_palindrome(string):
    """
    srting: string
    """
    pos1 = 0
    pos2 = len(string)-1-pos1
    while pos1 < pos2:
        if string[pos1] != string[pos2]:
            return False
        pos1 += 1
        pos2 -= 1
    return True

if __name__ == '__main__':
    n = sum_palindrome_base_2_and_10(int(1e6))
    print(n)
    
    
    