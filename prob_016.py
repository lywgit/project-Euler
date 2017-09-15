#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 13:18:35 2017
Problem 16 Power digit sum
@author: lywang
"""
from prob_013 import int_str_sum


def show_power_digits(n):
    digit_size = len(str(int(2**n)))
    for i in range(1,n+1):
        print(str(2**i).zfill(digit_size))

def int_str_multiply_single_digit(a, b_single):
    result = ''
    b = int(b_single)
    carry = 0
    for i in reversed(range(len(a))):
        m = int(a[i]) * b + carry
        if m >= 10:
            carry = m//10
            m = m - carry*10
        else:
            carry = 0
        result  = str(m) + result
    if carry:
        result  = str(carry) + result
    return result
    

def int_str_multiply(a, b):
    if len(a) < len(b):
        temp = b
        b = a
        a = temp
    place = 0
    result = '0'
    for i in reversed(range(len(b))):
        temp = int_str_multiply_single_digit(a, b[i]) + place * '0'
        result = int_str_sum(result, temp)
        place += 1
    return result
        
def int_str_power(base, power):
    result = '1'
    for i in range(int(power)):
        result = int_str_multiply(base, result)
    return result

def int_str_digit_sum(n):
    result = 0
    for i in range(len(n)):
        result += int(n[i])
    return result

#show_power_digits(100)
if __name__ == '__main__':
    int_string = int_str_power('2', '1000')
    print(int_str_digit_sum(int_string))
