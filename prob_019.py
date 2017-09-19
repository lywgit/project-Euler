#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 18:37:51 2017
Problem 19 Counting Sundays
@author: lywang
"""



def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
    
def days_per_month(year, month):
    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    elif month in [4,6,9,11]:
        return 30
    else: # 1, 3, 5, 7, 8, 10, 12
        return 31 

def next_month(year, month):
    if month != 12:
        return (year, month+1)
    else:
        return (year+1, 1)


def days_since_1900(year, month, day):
    # return 1 for 1900-01-01
    assert(year >= 1900)
    y = 1900
    m = 1
    day_diff = 0
    while (y, m) != (year, month):
        day_diff += days_per_month(y, m)
        (y, m) = next_month(y, m)
    day_diff += day   
    return day_diff 
    
def is_sunday(year, month, day):
    # 1900-01-01 was a Monday
    day_diff = days_since_1900(year, month, day)
    return day_diff % 7 == 0


def count_sunday():
    count = 0
    for year in range(1901, 2001):
        for month in range(1,13):
            if is_sunday(year, month, 1):
                count += 1
            #print("{0}-{1}-1: {2}".format(year, month, is_sunday(year, month, 1)))
    return count
        

if __name__ == '__main__':
    print(count_sunday())








 