#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 17:57:46 2017
Problem 33 Digit cancelling fractions
@author: lywang

Note: 
    The logic seems ugly, better use more fundamental approach
    (like fraction operation)
"""
from prob_012 import factorize

def search_fractions():
    """
    denumeratot = AB  = tens ones  
     iA      i             Bi      i
    ---- == ---  (i<B) or ---- == --- (i<A)
     AB      B             AB      A
    
    """
    matches = []
    for denominator in range(11,100):
        A, B = denominator // 10, denominator % 10
        if B == 0:
            continue
        for i in range(1, max(A, B)):
            # possibility 1
            fraction = (i*10 + A, denominator)
            cancelled = (i, B)
            if is_equal_fraction(fraction, cancelled):
                matches.append(fraction)
            # possibility 2
            if B <= A:
                fraction = (B*10 + i, denominator)
                cancelled = (i, A)
                if is_equal_fraction(fraction, cancelled):
                    matches.append(fraction)
    return matches

def is_equal_fraction(a, b):
    # represeting fraction with tuple (numerator, denomiator)
    return a[0]*b[1] == a[1]*b[0]


def numerator_denumerator_product(fractions):
    numerator_product = 1
    denominator_product = 1
    for fraction in fractions:
        numerator_product *= fraction[0]
        denominator_product *= fraction[1]
    return numerator_product, denominator_product

def reduced_fraction(fraction):
    [numerator, denominator] = list(fraction)
    denominator_factors, expo = factorize(denominator)
    for n in denominator_factors:
        while numerator % n == 0 and denominator % n == 0:
            [numerator, denominator] = numerator // n, denominator //n
    return numerator, denominator
  
if __name__ == '__main__':
    matches = search_fractions()
    print(matches)
    num, deno = numerator_denumerator_product(matches)
    print(num, deno)
    result = reduced_fraction((num, deno))
    print(result)
    
    