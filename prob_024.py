#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 13:12:33 2017
Problem 24 Lexicographic permutations
@author: lywang

Idea: 
    The numbers can be grouped hierarchically from the largests
    digit place to the smallest digit place. Take digits [0, 1, 2]
    as example. The first three groups are 0xx < 1xx < 2xx, and 
    there are 2!=6 numbers in each group. Then, in the second group
    there are two subgroups: 0x < 2x, each containing 1!=1 numbers.
    
"""

import unittest
from prob_015 import factorial


def hierarchy_indices(query, divisors):
    """
    hierarchy_indices(4, [2,1]) returns [2,0,0]
            |    
    4 = 2 * 2 + 0
    0 = 1 * 0 + 0
            0
            |
    """
    indices = []
    for d in divisors:
        #print("{0} = {1} * {2} + {3} ".format(query, d, query//d, query%d))
        indices.append(query//d)
        query = query % d
    indices.append(0) 
    return indices

def arranged_digits(hierarchy_indices, digits):
    """
    arranged_digits([2,0,0], [0,1,2]) returns [2, 0, 1]
    """
    available_digits = digits[:]
    result = []
    for i in hierarchy_indices:
        value = available_digits[i]
        result.append(value) 
        available_digits.remove(value)
    return result
    

def lexicographic_permutation(digits, query_permutation):
    """
    query_permutation is 1-based    
    """
    num_digits = len(digits)
    q = query_permutation - 1 # zero-based
    divisors = [factorial(i) for i in reversed(range(1,num_digits))]
    indices = hierarchy_indices(q, divisors)
    result = arranged_digits(indices, digits)
    return result


class Test(unittest.TestCase):
    def test_hierarchy_indices(self):
        divisors = [6, 2, 1]
        self.assertEqual(hierarchy_indices(7, divisors), [1,0,1,0])
    def test_arranged_digits(self):
        digits = [0, 1, 2]
        self.assertEqual(arranged_digits([0,0,0], digits), [0,1,2])
        self.assertEqual(arranged_digits([2,1,0], digits), [2,1,0])
        self.assertEqual(arranged_digits([2,0,0], digits), [2,0,1])
    def test_lexicographic_permutation(self):
        digits = [0, 1, 2]
        self.assertEqual(lexicographic_permutation(digits, 4), [1,2,0])

if __name__ == '__main__':
    #unittest.main()
    digits = [i for i in range(10)]
    query = int(1e6)
    print(lexicographic_permutation(digits, query))



