#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 17:46:28 2017
Problem 30 Digit fifth powers
@author: lywang
"""
import math

def is_digit_power_sum(n, power):
    digit_power_sum = 0
    n_copy = n
    while n_copy > 0:
        digit_power_sum += (n_copy%10)**power
        n_copy //= 10
    #print(n, digit_power_sum)
    return n == digit_power_sum

def possible_digit_range(power):
    num_digits = 1
    while True:
        digit_power_sum = num_digits * 9**power
        #print(num_digits, digit_power_sum, math.log10(digit_power_sum)+1)
        if num_digits >= int(math.log10(digit_power_sum))+1:
            break
        num_digits += 1
    return num_digits

def search_digit_power_numbers(power):
    match = []
    limit = 10**possible_digit_range(power)-1
    for i in range(2, limit):
        if is_digit_power_sum(i, power):
            match.append(i)
    return match


if __name__ == '__main__':
    power = 5
    numbers = search_digit_power_numbers(power)
    print(numbers)
    print('sum: ', sum(numbers))
