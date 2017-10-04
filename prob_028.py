#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 16:26:11 2017
Problem 28 Number spiral diagonals 
@author: lywang
"""

def layer_number(edge_length):
    # 1-based
    return (edge_length+1)//2

def diagonals(layer):
    if layer == 1:
        return [1]
    else:
        edge_length = (layer-1)*2 + 1
        numbers = [edge_length**2 -i*(edge_length-1) for i in range(4)] 
    return numbers

def diagonals_sum(max_layer):    
    diagonals_sums = [sum(diagonals(layer)) for layer in range(1, max_layer+1)]
    total_sum = sum(diagonals_sums)
    
    return total_sum

if __name__ == '__main__':
    layer = layer_number(1001)
    print(diagonals_sum(layer))