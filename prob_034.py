#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 11:03:02 2017
Problem 34 Digit factorials
@author: lywang

Idea:
    9! = 40320
    At most 6 sigit is possible. 
    (40320*7 = 282240 is at most 6 digit)
"""

from prob_015 import factorial


def search():
    factorials = [factorial(x) for x in range(10)]
    matches = []
    limit = int(1e7)
    for i in range(limit):
        if i == digit_factorial_sum(i, factorials):
            #print(i)
            matches.append(i)
    return matches


def digit_factorial_sum(number, factorial_table):
    f_sum = 0 
    digit = number % 10
    f_sum += factorial_table[digit]
    number //= 10 
    while number:
        digit = number % 10
        f_sum += factorial_table[digit]
        number //= 10
    return f_sum

if __name__ == '__main__':
    matches = search()
    matches.remove(1)
    matches.remove(2)
    print(sum(matches))