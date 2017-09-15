#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 12:23:06 2017
Problem 15 Lattice paths
@author: lywang
"""

def factor(i):
    if i==1:
        return 1
    else:
        return i * factor(i-1)
    
def lattice_paths(shape):
    n1 = shape[0]
    n2 = shape[1]
    return factor(n1+n2) // (factor(n1)*factor(n2)) # integer division


""" 
key idea: for 2x2 grid, you need 2 Right & 2 Down to get there. 
Find combinations of possible distrinct arrangement
"""
if __name__ == "__main__":
    print(lattice_paths([20,20]))

