#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 10:29:36 2017
Problem 25 1000-digit Fibonacci number
@author: lywang
"""

import math
import unittest

def fibonacci(i):
    if i == 1 or i == 2:
        return 1
    else:
        return fibonacci(i-1) + fibonacci(i-2)

def fibonacci_generator():
    yield 1
    yield 1
    previous_2 = 1
    previous_1 = 1
    while True:
        current = previous_2 + previous_1
        yield current
        (previous_2, previous_1) = (previous_1, current)
        #yield output

def min_n_digits_fibonacci(n):
    fibonacci = fibonacci_generator()
    i = 1 
    F_i = next(fibonacci)
    while math.log10(F_i)< n-1 :
        i += 1
        F_i = next(fibonacci)
        #print(i, F_i, math.log10(F_i))
    return (i, F_i, math.log10(F_i))
    

class Test(unittest.TestCase):
    def test_fibonacci_generator(self):
        fibonacci = fibonacci_generator()
        F = []
        for i in range(10):
            F.append(next(fibonacci))
        self.assertEqual(F, [1,1,2,3,5,8,13,21,34,55])
    
    def test_min_n_digits_fibonacci(self):
        i, F_i, log10F_i = min_n_digits_fibonacci(3)
        self.assertEqual([i, F_i], [12, 144])        

if __name__ == '__main__':
    #unittest.main()
    i, F_i, log10F_i = min_n_digits_fibonacci(1000)
    print(i)
    
    
    