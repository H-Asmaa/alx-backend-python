#!/usr/bin/env python3
"""0x00-python_variable_annotations"""
from typing import List, Union, Tuple


def to_kv(k: str, v: [Union[int, float]]) -> Tuple[Union[str, float]]:
    """A function that uses variable annotation, takes a string k and a
    v being float or an int, and returns a tuple of mixed elements."""
    return (k, v * v)
