#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 16:27:21 2017
Problem 9
@author: lywang
"""


def is_pathagorean(a, b, c):
    assert(c>a and c>b and b>a)
    return a**2 + b**2 == c**2

def loop_triplet(triplet_sum):
    a = 1 
    while a <= triplet_sum:
        b = a+1
        while a+b <= triplet_sum:
            c = triplet_sum - a - b
            if c>b:
                if is_pathagorean(a, b, c):
                    print(a,b,c)
                    print(a*b*c)
                
            b += 1
        a += 1
        


# main
if __name__ == '__main__':
    loop_triplet(1000)