#!/usr/bin/env python

"""
Write code to raise a number to a power.

Possible questions to ask:
1. What is the data type of the number?
2. What is the data range of the power?

Time complexity: O(logP)
"""


def power(n, p):
    if p == 0:
        return 1
    if p == 1:
        return n
    odd = (p % 2)
    half = p >> 1
    half_val = power(n, half)
    if odd:
        return half_val * half_val * n
    else:
        return half_val * half_val