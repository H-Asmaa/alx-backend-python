#!/usr/bin/env python3
"""0x00-python_variable_annotations"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """A function that we must add the variable annotation to."""
    return [(i, len(i)) for i in lst]
