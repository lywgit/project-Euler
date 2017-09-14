#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 17:49:14 2017
problem 10
@author: lywang
"""

import math

def is_prime(q):
    if q == 1:
        return False
    elif q == 2:
        return True
    else:
        max_factor = math.ceil(math.sqrt(q))
        for factor in range(2, max_factor+1):
            if q % factor == 0:
                return False
        return True
            
def prime_sum(limit):
    summation = 0
    for i in range(1, limit):
        if is_prime(i):
            summation += i
    return summation

        
# main
if __name__ == '__main__':
    print(prime_sum(int(2e6)))