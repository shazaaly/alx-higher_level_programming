#!/usr/bin/python3
"""
This is the 0-add_integer module.
It contains a function for adding two integers or floats.

"""


def add_integer(a, b=98):
    """Args: a,b two floats or integers
       Return an integer: sum of 2 numbers
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, int):
        raise TypeError("b must be an integer or float")
    return a + b
