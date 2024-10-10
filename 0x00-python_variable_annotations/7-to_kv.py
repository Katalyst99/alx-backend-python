#!/usr/bin/env python3
"""The module for a type-annotated function to_kv"""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """
    Function that takes a string k and an int OR float v as arguments,
    and returns a tuple.
    """
    return k, v**2
