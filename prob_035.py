#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 11:17:39 2017

@author: lywang

Problem 35 Circular primes
"""

import unittest
from prob_010 import is_prime


def circular_primes(limit):
    primes = prime_set(limit)
    circ_primes = set()
    for i in primes:
        if i not in circ_primes:
            rotations = set(rotation_of(i))
            if rotations.issubset(primes):
                circ_primes.update(rotations)
    return circ_primes

def prime_set(limit):
    return {i for i in range(1,int(limit)) if is_prime(i) }

def rotation_of(n):
    rotations = [n]
    l = list(str(n))
    for i in range(len(l)-1):
        l.insert(0, l.pop())
        rotations.append( int( "".join(l) ) )
    return rotations
    
class Test(unittest.TestCase):
    def test_prime_set(self):
        self.assertEqual(prime_set(20), {2,3,5,7,11,13,17,19})
    
    def test_rotation_of(self):
        self.assertEqual(rotation_of(123), [123, 312, 231])
        
    def test_circular_primes(self):
        self.assertEqual(circular_primes(100), 
                         {2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97})
    

if __name__ == '__main__':
    #unittest.main()
    circ = circular_primes(1e6)
    #print(sorted(circ))
    print(len(circ))
    

