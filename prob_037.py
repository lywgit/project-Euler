#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 14:57:02 2017

@author: lywang

Problem 37 Truncatable primes
"""

from prob_010 import is_prime

def is_truncatable_prime(n):
    if not is_prime(n) or n < 10:
        return False
    s = str(n)
    for i in range(1,len(s)):
        #print(s[i:], s[:-i])
        if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
            return False    
    return True


if __name__ == '__main__':
    trunc_primes = []
    i = 1
    while len(trunc_primes) < 11:
        if is_truncatable_prime(i):
            trunc_primes.append(i)
        i += 1
    print(trunc_primes)
    print('Sum: ', sum(trunc_primes))
        

