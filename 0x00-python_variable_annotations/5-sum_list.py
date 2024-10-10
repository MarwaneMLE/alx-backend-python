#!/usr/bin/env python3
"""
Annotation function that takes input list of float and return sum of
ltts element as float
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Return sum of float values in input list"""
    return float(sum(input_list))
