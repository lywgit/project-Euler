#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 13:03:49 2017
Problem 22 Names scores
@author: lywang
"""
import unittest    

def read_names_file(file_name):
    with open(file_name) as f:
        data = f.read()
    f.close()
    data = data.split(',')
    data = [s.strip('"') for s in data]
    return data

def alphabetical_value(string):
    reference_value = ord('A') - 1
    numbers = [ord(c)-reference_value for c in string]
    return sum(numbers)

def name_scores(data):
    data.sort()
    scores = [alphabetical_value(name)*(i+1) for i, name in enumerate(data)]
    return scores

class Test(unittest.TestCase):
    def test_alphabetical_value(self):
        self.assertEqual(alphabetical_value('COLIN'), 53)

if __name__ == '__main__':
    #unittest.main()
    data = read_names_file('p022_names.txt')
    print(sum(name_scores(data)))
        
    