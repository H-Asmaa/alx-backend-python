#!/usr/bin/env python3
"""0x00-python_variable_annotations"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """A function that uses variable annotation, takes a float and returns
    a function that multiplies the multiplier by an n."""
    def inner_multiplier(n: float):
        return n * multiplier
    return inner_multiplier
