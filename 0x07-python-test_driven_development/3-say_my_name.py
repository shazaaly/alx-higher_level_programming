#!/usr/bin/python3
""" This module is about a function to prints My name."""


def say_my_name(first_name, last_name=""):
    """Args: first_name, last_name two strings
       Return : void, prints full name.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if first_name and last_name:
        print("My name is: {} {}".format(first_name, last_name))

    else:
        print("My name is: {}".format(first_name))
        return
