#!/usr/bin/env python3
"""The module 10. Duck typing - first element of a sequence"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the correct duck-typed annotations(first element)"""
    if lst:
        return lst[0]
    else:
        return None
