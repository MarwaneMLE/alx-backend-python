#!/usr/bin/env python3
"""
Annotation method that takes mixed list of integers and float
and return sum as float
"""


def sum_mixed_list(mxd_list: list) -> float:
    """Sum of mixed int and float in list and return float"""
    sum_mxd_list = 0
    for value in mxd_list:
        if value is int:
            value = float(value)
        sum_mxd_list += value
    return sum_mxd_list
