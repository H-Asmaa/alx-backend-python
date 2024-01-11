#!/usr/bin/env python3
"""0x00-python_variable_annotations"""
from typing import Sequence, Any, Union
from types import NoneType

def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    """A function that we must add the variable annotation to."""
    if lst:
        return lst[0]
    else:
        return None
