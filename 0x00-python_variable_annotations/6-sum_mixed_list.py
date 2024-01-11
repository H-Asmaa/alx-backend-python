#!/usr/bin/env python3
"""0x00-python_variable_annotations"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """A function that uses variable annotation, takes in a
    list of floats and ints and returns the float sum of elements.
    It uses Union to declaire mixed elements."""
    return sum(mxd_lst, 0.0)
