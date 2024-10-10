#!/usr/bin/env python3
"""
Annotation function that takes input list of float and return sum of
ltts element as float
"""


def sum_list(input_list: list) -> float:
    """ Return sum of float values in input list"""
    sum = 0
    for value in input_list:
        sum += value
    return sum
