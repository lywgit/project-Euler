#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 10:46:35 2017
Problem 14 Longest Collatz sequence
@author: lywang
"""


def next_Collatz(n):
    if n % 2 == 0:
        return n/2
    else:
        return 3*n+1

# straight forward version works fine
def chain_length(i):
    if i == 1:
        return 1
    return chain_length(next_Collatz(i)) + 1
   
def max_chain_length(n):
    max_length = 0
    max_length_i = 0
    for i in range(1, n):
        l = chain_length(i) 
        if l > max_length:
            max_length = l 
            max_length_i = i
    return (max_length_i, max_length)

# improve speed by keeoping a record and avoid repeated effort
def length_record(i, record):
    if i in record:
        return record[i], record 
    else:
        length, record = length_record(next_Collatz(i), record)
        record[i] = length + 1
        return record[i], record
    

def max_chain_length_record(n):
    record = {1: 1}
    max_length = 0
    max_length_i = 0
    for i in range(1, n):
        l, record = length_record(i, record) 
        if l > max_length:
            max_length = l 
            max_length_i = i
    return (max_length_i, max_length)
    



if __name__ == '__main__':
    import time 
    t_start = time.time()
    i, l = max_chain_length(int(1e6))
    print("max length index: ", i, "  (max length: ", l, ")")
    t_end = time.time()
    print("Ellapse time: ", t_end - t_start)
    
    t_start = time.time()
    i, l = max_chain_length_record(int(1e6))
    print("max length index: ", i, "  (max length: ", l, ")")
    t_end = time.time()
    print("Ellapse time: ", t_end - t_start)
    
    
    
    
    
    
