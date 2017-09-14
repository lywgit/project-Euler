#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 10:49:18 2017
Problem 12 Highly divisible triangular number
@author: lywang
"""

import math
from prob_010 import is_prime

def factorize(q):
    factors = []
    exponents = []
    max_possible_prime_factor = math.ceil(math.sqrt(q))
    for i in range(1, max_possible_prime_factor+1):
        if is_prime(i) and q % i == 0:
            factors.append(i)
            count = 0
            while q % i == 0:
                q //= i  # int division 
                count += 1
            exponents.append(count)
            if q == 1:
                break
    if is_prime(q):
        factors.append(q)
        exponents.append(1)
    return (factors, exponents)

def num_divisors(k):
    _, exponents = factorize(k)
    combination = 1
    for expo in exponents:
        combination *= (expo + 1)
    return combination

def first_triangle_with_k_plus_divosor(k):
    natural = 1
    triangle_number = 1
    n_d = num_divisors(triangle_number)
    while n_d < k:
        natural += 1
        triangle_number += natural
        n_d = num_divisors(triangle_number)
        #print(triangle_number, n_d)
    return triangle_number
            

if __name__ == '__main__':
    print(first_triangle_with_k_plus_divosor(500))

