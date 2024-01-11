#!/usr/bin/env python3
"""0x00-python_variable_annotations"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """A function that uses variable annotation, takes in a
    list of floats and returns the float sum of elements."""
    return sum(input_list, 0.0)
