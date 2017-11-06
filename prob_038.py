#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 15:46:35 2017

@author: lywang

Problem 38 Pandigital multiples

"""

import unittest
from prob_032 import permutation_generator, digits_to_int

def is_concatenated_product(a):
    s = str(a)
    for i in range(1, len(s)//2+1):
        a = int(s[:i])
        if s in [concatenated_product_str(a, j) for j in range(1,len(s))]:
            #print(s)
            return True
    return False
        
def concatenated_product_str(a, n):
    return "".join([str(a * i) for i in range(1, n+1)])

def is_9_pandigital(i):
    s = str(i)
    if len(s)==9 and set(s)==set('123456789'):
        return True
    else:
        return False

class Test(unittest.TestCase):
    def test_is_9_pandigital(self):
        self.assertEqual([is_9_pandigital(123456789), 
                          is_9_pandigital(123456788),
                          is_9_pandigital(12345678)] , 
                          [True, False, False] ) 
    def test_concatenated_product_str(self):
        self.assertEqual(concatenated_product_str(192, 3), '192384576')
        
    def test_is_concatenated_product(self):
        self.assertEqual(is_concatenated_product(918273645), True)
        self.assertEqual(is_concatenated_product(192384576), True)
        self.assertEqual(is_concatenated_product(123456789), False)
       
if __name__ == '__main__':
    unittest.main()
    generator = permutation_generator(list('987654321'))
    while True:
        i = digits_to_int(next(generator))
        if is_9_pandigital(i) and is_concatenated_product(i):
                print(i)
                break

