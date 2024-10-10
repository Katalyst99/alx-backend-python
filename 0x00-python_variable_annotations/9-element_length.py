#!/usr/bin/env python3
"""The module for 9. Let's duck type an iterable object"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function returns a list of tuples(duck typing)
    """
    return [(i, len(i)) for i in lst]
