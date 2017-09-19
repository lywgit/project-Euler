#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 12:48:21 2017
Problem 67 Maximum path sum II
@author: lywang
"""

from prob_018 import max_path_sum

def read_triangle_data(file_name):
    with open(file_name) as f:
        data = f.read()
    f.close()
    values = [int(i) for i in data.split()]
    return values



if __name__ == '__main__':
    values = read_triangle_data('p067_triangle.txt')
    print(max_path_sum(values)[0])

