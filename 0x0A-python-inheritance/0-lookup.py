#!/usr/bin/python3
"""This module is about Write a function that returns the list
of available attributes and methods of an object"""


def lookup(obj):
    """
    function that returns the list of attributes and methods of an object.
    Args: object
    Returns: a list of attributes and methods of an object
    """

    return dir(obj)
