#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 10:57:29 2017
Problem 20 Factorial digit sum
@author: lywang
"""

from prob_016 import int_str_multiply, int_str_digit_sum


def int_str_factor(n):
    if n == '1':
        return '1'
    else:
        return int_str_multiply(n, int_str_factor(str(int(n)-1)))
        # int(n) relies on python's ability to handle int, otherwise should 
        # write a int_str_addition that handles munus operation to do this

if __name__ == '__main__':
    print(int_str_digit_sum(int_str_factor('100')))


