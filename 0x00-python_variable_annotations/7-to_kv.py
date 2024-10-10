#!/usr/bin/env python3
"""
Annotation funct that takes s astring or float as args
and return a tuple
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ method that return the tuple of two inputs str and flaot or int."""
    return (k, float(v**2))
