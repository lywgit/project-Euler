#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 10:28:27 2017
Problem 32 Pandigital products
@author: lywang

Idea:
    Each permutation is uniquely determined by a hierarchical index
    Take the set ["A","B","C"] for example. A zero-based hiararchical
    index of [1,0,0] means picking the 2nd element ("B") and remove it 
    from the set. And then pick the first from remaining set 
    ["A","C"] which is "A" and remove it, finally pick the first of the 
    remaining set ["C"] which is "C". So [1,0,0] => ["B","A","C"]
    The range of hierarchical index will be [0-2,0-1,0-0] in this case.

Note:
    The digit_to_int function takes up most time. using a lower level
    representation of digits should help
    
"""


def search_pandigital_products(digits):
    match = []
    permutation = permutation_generator(digits)
    for sequence in permutation:
        split = split_generator(sequence)
        for numbers in split:
            if is_product(*numbers):
                match.append(numbers)
    return match


def is_product(a, b, c):
    return a*b == c

def permutation_generator(elements):
    index_cap = [i for i in reversed(range(len(elements)))]
    index = [0] * len(elements)
    result = translate(index, elements)
    #print(index, translate(index, elements))
    yield result
    while index != index_cap:
        increase_index(index, index_cap)
        result = translate(index, elements)
        #print(index, translate(index, elements))
        yield result


def translate(index, elements):
    elements_copy = elements[:]
    result = []
    for i in index:
        result.append(elements_copy[i])
        elements_copy.remove(elements_copy[i])
    return result

def increase_index(index, cap):
    index[-1] += 1
    i = -1
    while index[i] > cap[i]:
        index[i] = 0
        index[i-1] +=1
        i -= 1
    return index

def split_generator(sequence):
    n = len(sequence)
    for i in range(1,n-1):
        a = digits_to_int(sequence[:i])
        for j in range(i+1, n):
            b = digits_to_int(sequence[i:j])
            c = digits_to_int(sequence[j:]) 
            yield (a,b,c)
           

def digits_to_int(digits):
    s  = ''.join(map(str, digits))
    return int(s)

def unique_product_sum(match):
    products = [numbers[2] for numbers in match]
    unique_product = set(products)
    return sum(unique_product)
        
if __name__ == "__main__":
    digits = [i for i in range(1,10)]
    match = search_pandigital_products(digits)
    print(match)
    product_sum = unique_product_sum(match)
    print("sum: ", product_sum)










