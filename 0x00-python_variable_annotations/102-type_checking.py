#!/usr/bin/env python3
"""0x00-python_variable_annotations"""
from typing import Tuple, List, Union, Generator


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """A function that needed fixing of annotation and much more."""
    zoomed_in: Generator = (item for item in lst for i in range(factor))
    return list(zoomed_in)


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
