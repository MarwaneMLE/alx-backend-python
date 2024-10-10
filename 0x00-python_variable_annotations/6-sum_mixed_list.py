#!/usr/bin/env python3
"""
Annotation method that takes mixed list of integers and float
and return sum as float
"""


from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Sum of mixed int and float in list and return float"""
    return float(sum(mxd_list))
