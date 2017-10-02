#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 14:25:56 2017
Problem 26 Reciprocal cycles
@author: lywang

Note:
    Need precise sequence of decimal part, python class Decimal may be 
    useful. But I wrote a function for precise_division anyway.

Hindsight: 
    1/d can have at most d-1 recuring digits
    This is understood by nature of mod. Using an integer d as
    divisor, the value of remainder can only be one of 
    {0,1,..., d-1}. 0 means that d is a factor of the dividend
    and there won't be any recurring part. The rest may be cycled 
    through so at most d-1 digits.

"""
 

def max_reciprocal_recurring_length(search_range):
    max_length = 0
    max_length_reciprocal_i = 0
    for i in range(2, search_range+1):
        head, recuring = parse_reciprocal_recursion(i)
        if len(recuring) > max_length:
            max_length_reciprocal_i = i
            max_length = len(recuring) 
    return (max_length_reciprocal_i, max_length)

def print_reciprocal(a):
    (head, recursion) = parse_reciprocal_recursion(a)
    if recursion == '0':
        print("1/{} = {}".format(a, head))
    else:
        print("1/{} = {}({})".format(a, head, recursion)) 

def parse_reciprocal_recursion(a):
    precision = 2*a
    sequence = precise_division(1, a, precision)

    head_length = 0
    while head_length <= len(sequence)/2:
        #print(sequence[head_length:])
        recursion_length = find_recursion_length(sequence[head_length:])
        if recursion_length != None:
            break
        head_length += 1
    
    if recursion_length == None:
        print("Should raise precision.")
    head = sequence[0:head_length]
    recursion = sequence[head_length:head_length+recursion_length];
    #print_reciprocal(a, head, recursion)
    return (head, recursion)

def find_recursion_length(sequence):
    pattern_length = 1
    while pattern_length*2 < len(sequence) : 
        pattern = sequence[:pattern_length]
        if is_recurring(sequence, pattern):
            return pattern_length
        pattern_length += 1
    return None

def is_recurring(sequence, pattern):
    pattern_length = len(pattern)
    i = 1
    while (i+1) * pattern_length < len(sequence):
        if sequence[i*pattern_length:(i+1)*pattern_length] != pattern:
            return False
        i += 1
    return True
    


def precise_division(dividend, divisor, decimal_places):
    quotient_str = str(dividend // divisor)
    remainder = dividend % divisor
    quotient_str += '.'
    if remainder == 0:
        quotient_str += decimal_places * '0'
    else:
        place = 0
        while place < decimal_places:
            remainder *= 10
            if remainder < divisor:
                quotient_str += '0'
            else:
                quotient_str += str(remainder // divisor)
                remainder = remainder % divisor
            place += 1
    return quotient_str


if __name__ == '__main__':
    search_range = 100
    i, recuring_length = max_reciprocal_recurring_length(search_range)
    print("Integers below {} with longest reciprocal recurring cycle is {}".format(search_range, i))
    print_reciprocal(i)




