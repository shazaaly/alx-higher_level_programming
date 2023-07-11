#!/usr/bin/python3
"""
This module is to check  if the object is exactly
an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    check  if the object is exactly an instance of the specified class
    Args :  object and class names
    Returns : True or False
    """

    return type(obj) is a_class
