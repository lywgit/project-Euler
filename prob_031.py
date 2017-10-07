#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 21:49:26 2017
Problem 31 Coin sums
@author: lywang
"""




def combinations(amount, coins, record=[]):
    # Assumes coins in descending order and the last coin value is 1 
    record_copy = record[:]
    if len(coins) == 1:
        record_copy.append(amount//coins[0])
        #print(record_copy)
        return 1
    if amount == 0:
        record_copy.extend([0]*len(coins))
        #print(record_copy)
        return 1
    num_ways = 0
    coin_value = coins[0]
    coin_count = 0
    while amount >= 0:
        record_copy = record[:]
        record_copy.append(coin_count)
        num_ways += combinations(amount, coins[1:], record_copy)
        coin_count += 1
        amount -= coin_value
    return num_ways


if __name__ == '__main__':
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    print(combinations(200, coins))

