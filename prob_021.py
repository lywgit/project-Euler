#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 11:26:51 2017
Problem 21 Amicable numbers
@author: lywang
"""

import math

def proper_divisors(n):
    if n == 1:
        return []
    divisors = [1]
    floor_sqrt_n = math.floor(math.sqrt(n))
    for i in range(2, floor_sqrt_n+1):
        if n % i == 0:
            if i == n//i:
                divisors.append(i)
            else:
                divisors.extend([i, n//i])
        i += 1
    divisors.sort()
    return divisors


def proper_divisors_sum(n):
    return sum(proper_divisors(n))

def amicable_number(a):
    b = proper_divisors_sum(a)
    if a != b and a == proper_divisors_sum(b):
        return b
    else:
        return None
    
def search_amicable_numbers(limit):
    amicable_numbers = set()
    for a in range(1, limit):
        b = amicable_number(a)
        if b:
            amicable_numbers.update([a])
            if b <limit:
                amicable_numbers.update([b])
    return amicable_numbers
    
if __name__ == '__main__':
    amicables = search_amicable_numbers(10000)
    print(amicables)
    print(sum(amicables))
    
    
    
    