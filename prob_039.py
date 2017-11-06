#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 11:47:53 2017

@author: lywang

Problem 39 Integer right triangles

"""

from prob_009 import is_pathagorean


def pathagorean_of_max_perimeter(p_max):
    """
    a < b < c; a+b+c=p
    """
    pathagoreans = []
    for p in range(1, p_max+1):
        a_max = p_max//3
        for a in range(1, a_max):
            b_max = (p-a)//2
            for b in range(a+1, b_max):
                c = p-a-b
                #print((a,b,c), is_pathagorean(a,b,c))
                if is_pathagorean(a,b,c):
                    pathagoreans.append((a,b,c))
                    #print(p, (a,b,c))
    return pathagoreans


if __name__ == '__main__':
    pathagoreans = pathagorean_of_max_perimeter(1000)
    perimeters = [sum(t) for t in pathagoreans]
    p_max_solutions = max(perimeters, key=perimeters.count)
    # see https://stackoverflow.com/a/40785493
    print(p_max_solutions)