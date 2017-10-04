#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 11:26:10 2017
Problem 27 Quadratic primes
@author: lywang
"""

from prob_010 import is_prime

def prime_list(bound):
    primes = []
    for i in range(1, bound+1):
        if is_prime(i):
            primes.append(i)
    return primes

def get_quadratic_formula(a, b):
    def quadratic(n):
        return n**2 + a*n + b
    return quadratic

def search_loop(a_bound_exclusive, b_bound_inclusive):
    max_prime_abn = (0, 0, 0)
    for a in range(-a_bound_exclusive+1, a_bound_exclusive):
        for b in range(-b_bound_inclusive, b_bound_inclusive+1):
            quadratic = get_quadratic_formula(a, b)
            n = 0
            while quadratic(n)>0 and is_prime(quadratic(n)):
                n += 1
            if n > max_prime_abn[2]:
                max_prime_abn = (a, b, n)
                print('New record (a,b,n): ', max_prime_abn)
    return max_prime_abn
    


if __name__ == "__main__":
    a, b, n = search_loop(1000, 1000)
    print("Final best: a = {}, b = {}, n = {}, a*b = {}".format(a,b,n,a*b))
    
    
    