#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 15:51:34 2017
Problem 23 Non-abundant sums
@author: lywang
"""

import unittest

from prob_021 import proper_divisors_sum

def is_abundant_number(n):
    return proper_divisors_sum(n) > n

def abundant_number_list(cap):
    abundant_numbers = []
    for i in range(1, cap+1):
        if is_abundant_number(i):
            abundant_numbers.append(i)
    return abundant_numbers

def unique(ascending_list):
    unique_list = [ascending_list[0]]
    for i in range(1, len(ascending_list)):
        if ascending_list[i] != unique_list[-1]:
            unique_list.append(ascending_list[i])
    return unique_list

def possible_two_number_sum_values(numbers, cap):
    sums = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            s = numbers[i]+numbers[j]
            if s <= cap:
                sums.append(s)
    sums.sort()
    sums = unique(sums)
    return sums


def not_two_abundant_number_sum(cap):
    abundant = abundant_number_list(cap)
    possible_two_sum_values = possible_two_number_sum_values(abundant, cap)      
    total_sum = (1+cap)*cap//2 
    return total_sum - sum(possible_two_sum_values)

class Test(unittest.TestCase):
    def test_is_abundant_number(self):
        self.assertEqual(is_abundant_number(12), True)
    def test_unique(self):
        l = [1,1,2,2,2,3,4,5,5]
        self.assertEqual(unique(l), [1,2,3,4,5])

        
if __name__ == '__main__':
    #unittest.main()
    cap = 28132
    result = not_two_abundant_number_sum(cap)
    print(result)
    


