#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 13:29:28 2017
Problem 17 Number letter counts
@author: lywang
"""

def number_to_words(n):
    # for numbers 1~1000
    dict_1 = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five',
              6:'six',7:'seven',8:'eight',9:'nine',10:'ten',
              11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen',
              16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
    dict_2 = {20:'twenty', 30:'thirty', 40:'forty',50:'fifty',60:'sixty',
              70:'seventy', 80:'eighty',90:'nighty'}
    if n < 20:
        return dict_1[n] 
    elif n < 100:
        if n % 10 == 0:
            return dict_2[n]
        else:
            tens = n // 10 
            ones = n - tens * 10
            return dict_2[tens*10] + ' '   + dict_1[ones]
    elif n < 1000:        
        hundreds = n // 100
        if n % 100 == 0:
            return dict_1[hundreds] + ' hundred'
        else:            
            rest = n - hundreds * 100
            return dict_1[hundreds] + ' hundred and ' + number_to_words(rest)
    elif n == 1000:
        return 'one thousand'
            

if __name__ == '__main__':  
    count = 0
    words = [number_to_words(i) for i in range(1,1001)]
    words_strip = [ "".join(s.split()) for s in words]
    print(len("".join(words_strip)))



