#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:04:03 2017
Problem 18 Maximum path sum I
@author: lywang
"""

data = (
    """
    75
    95 64
    17 47 82
    18 35 87 10
    20 04 82 47 65
    19 01 23 75 03 34
    88 02 77 73 07 63 67
    99 65 04 28 06 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
    """ ).split()


values = [int(s) for s in data]




def level_array(length):
    levels = [] # level label starts from 0
    i = 0
    while len(levels) < length:
        levels.extend([i] * (i+1))
        i += 1
    return levels

def children_array(length):
    levels = level_array(length)
    left  = [None] * length
    right = [None] * length
    for index in range(length):
        level = levels[index]
        left[index] = index + level + 1
        right[index] = index + level + 2
    return (left, right)

def max_path_sum(values):
    n = len(values)
    left, right = children_array(n)
    max_sum = [None] * n
    for i in reversed(range(n)):
        if left[i] >= n: # assuming complete triangle 
            max_sum[i] = values[i]
        else:
            max_sum[i] = values[i] + max(max_sum[left[i]], max_sum[right[i]])
    return max_sum



if __name__ == "__main__":
    print(max_path_sum(values)[0])
    
    




