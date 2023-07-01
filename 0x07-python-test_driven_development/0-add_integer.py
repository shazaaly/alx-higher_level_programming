#!/usr/bin/python3
"""Defines a summation function."""


def add_integer(a, b=98):
    """
    Args: a, b
    Return an integer: sum of 2 numbers
    """
    # Cast a and b to integers if they are floats
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, int):
        raise TypeError("b must be an integer or float")
    return a + b
