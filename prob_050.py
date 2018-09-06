#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 12:53:57 2018

@author: lywang

Problem 50: Consecutive prime sum
"""


from prob_010 import is_prime


def get_prime_list(limit):
    prime_list = []
    x = 2
    while x < limit:
        if is_prime(x):
            prime_list.append(x)
            # print(x)
        x += 1
    return prime_list



if __name__ == '__main__':
    
    limit = int(1e6)
    prime_list = get_prime_list(limit)
    print('prime_list done.')
    
    n_longest = 1;
    index_longest = [0, 0]
    for i_head in range(len(prime_list)):
        prime_sum = prime_list[i_head]
        i_tail = i_head + n_longest # skip those shorter than current best
        while True:
            if i_tail>=len(prime_list) or prime_sum + prime_list[i_tail] > limit:
                break
            else:
                prime_sum = sum(prime_list[i_head:i_tail+1])
                if prime_sum in prime_list and i_tail - i_head + 1 > n_longest:
                    n_longest = i_tail - i_head + 1
                    index_longest = [i_head, i_tail]
                    print('{} (sum of {} consecutive primes)'.format(
                            prime_sum, n_longest))
                i_tail += 1
                
    l = prime_list[index_longest[0]:index_longest[1]+1]
    p = sum(l) 
    
    print('Below {}, prime {} can be wrriten as the sum of the most ({}) \
          consecutive primes'.format(limit, p, n_longest))
    #print('The primes are ', l)



