#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 17:37:12 2017
Problem 29 Distinct Powers
@author: lywang
"""

def distinct_powers(a_range, b_range):
    values =  set()
    for a in range(a_range[0], a_range[1]+1):
        for b  in range(b_range[0], b_range[1]+1):
            values.add(a**b)
    return values

if __name__ == '__main__':
    values = distinct_powers([2, 100], [2, 100])
    print(len(values))
            
