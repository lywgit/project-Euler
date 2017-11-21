#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:26:39 2017

@author: lywang

Problem 40: Champernowne's constant 
"""

import unittest

def nth_digit(n_query):
    """
    stage 1: 1 2 ... 9    (1-digit numbers, numbers_in_stage=9)
    stage 2: 10 11 ... 99 (2-digit numbers, numbers_in_stage=90)
    """
    i = n_query
    stage = 1
    digit_per_number = stage
    numbers_in_stage = 10**stage - 10**(stage-1)
    digits_in_stage =  numbers_in_stage * digit_per_number
    while i - digits_in_stage > 0:
        i -= digits_in_stage
        stage += 1
        digit_per_number = stage
        numbers_in_stage = 10**stage - 10**(stage-1)
        digits_in_stage =  numbers_in_stage * digit_per_number
    s =  str(10**(stage-1) + (i-1)//stage )
    return int( s[(i-1) % stage])


class Test(unittest.TestCase):
    def test_nth_digit(self):
        s0 = '123456789101112131415'
        s = ''
        for i in range(1, len(s0)+1):
            s += str(nth_digit(i))
        self.assertEqual(s, s0)
        s0 = '100101102'
        s = ''
        for i in range(190, 190+len(s0)):
             s += str(nth_digit(i))
        self.assertEqual(s, s0)

  
if __name__ == '__main__':
    unittest.main()
    value = 1
    for i in range(7):
        n = 10**i
        value *= nth_digit(n)
        print("n = {} -> digit = {}".format(n, nth_digit(n)))
    print("result = ", value)

    