#!/usr/bin/env python3
"""
Annotation funct that takes s astring or float as args
and return a tuple
"""


def to_kv(k: str, v: float or int) -> tuple:
    """ method that return the tuple of two inputs str and flaot or int."""
    return f"({k}, {v**2})"
