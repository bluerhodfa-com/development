#!/usr/bin/env python

"""
Project Euler.net
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
def get_divs(n):
    divs = [x for x in range(1,21) if n % x == 0]
#   print divs
    return divs

for i in range(20,999999999,20):
    if len(get_divs(i)) == 20:
        print get_divs(i),i
