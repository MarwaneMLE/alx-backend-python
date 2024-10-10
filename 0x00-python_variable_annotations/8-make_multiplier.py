#!/usr/bin/env python3
"""
Annotation funct that takes a float as  args and return
multiplies by the this float
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ method that multiplies a float by multiplier """
    return lambda x: x * multiplier
