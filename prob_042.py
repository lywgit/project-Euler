#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 23:37:42 2018

@author: lywang

Problem 42: Coded triangle numbers
"""

import unittest

ordAm1 = ord('A') - 1

def read_words_file(file_name):
    with open(file_name) as f:
        data = f.read()
    f.close()
    data = data.split(',')
    data = [s.strip('"') for s in data]
    return data


def word_value(word):
    return sum([ord(char) - ordAm1 for char in word])

def traingle_number(n):
    return n*(n+1)/2

class Test(unittest.TestCase):
    def test_word_value(self):
        self.assertEqual(word_value('A'), 1) # A = 1
        self.assertEqual(word_value('B'), 2) # B = 2
        self.assertEqual(word_value('SKY'), 55)
    def test_triangle_number(self):
        self.assertEqual(traingle_number(2), 3)
        self.assertEqual(traingle_number(10), 55)


if __name__ == '__main__':    
    unittest.main()
    words = read_words_file('./prob_042_words.txt')
    max_word_len = max([len(w) for w in words ])
    traingle_numbers = [traingle_number(i) for i in range(1, max_word_len*25+1)]
    num_traingle_words = sum([word_value(w) in traingle_numbers for w in words])
    print('Ans: there are ', num_traingle_words, ' triangle words in words.txt')


