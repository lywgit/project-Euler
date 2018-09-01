#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 19:41:20 2018

@author: lywang

Problem 45: Triangular, pentagonal, and hexagonal
"""

from math import sqrt
import unittest

def hexagonal_gen(n=1):
    # n should be an integer
    while True:
        yield n*(2*n-1)
        n += 1

def is_integer(x):
    return int(x) == x

def is_triangular(n):
    return is_integer((-1+sqrt(1+8*n))/2.0)

def is_pentagonal(n):
    return is_integer((1+sqrt(1+24*n))/6.0)

class Test(unittest.TestCase):
    def test_hexagonal_gen(self):
        h_gen = hexagonal_gen()
        for y in [1, 6, 15, 28, 45]:
            self.assertEqual(next(h_gen) ,y)        
    def test_is_integer(self):
        self.assertEqual(is_integer(100000), True)
        self.assertEqual(is_integer(100000.0000001), False)
    def test_is_triangular(self):
        self.assertEqual(is_triangular(15), True)
        self.assertEqual(is_triangular(14), False)
    def test_is_pentagonal(self):
        self.assertEqual(is_pentagonal(35), True)
        self.assertEqual(is_pentagonal(34), False)


if __name__ == '__main__':
    unittest.main()
    hex_gen = hexagonal_gen()  
    count = 0
    stop = 2
    while True:
        y = next(hex_gen)
        if is_pentagonal(y) and is_triangular(y):
            print('Found: ', y)
            count += 1
        if count == stop:
            print('Done, breaking')
            break
    
    

    
