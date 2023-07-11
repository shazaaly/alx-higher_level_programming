#!/usr/bin/python3
"""
This module provides a function to check whether an object
is an instance of a class that inherited (directly or indirectly)
"""


def inherits_from(obj, a_class):
    """
    Check whether the given object is a
    class that inherited (directly or indirectly)

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
    True if the object is an instance given object is a
    class that inherited (directly or indirectly), False otherwise.
    """

    return issubclass(type(obj), a_class)
