#!/usr/bin/env python3
"""The module for a type-annotated function make_multiplier"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """
    Function that takes a float multiplier as argument,
    and returns a function that multiplies a float by multiplier.
    """
    def multiply_float(n: float) -> float:
        """Function multiplies a float"""
        return multiplier * n
    return multiply_float
