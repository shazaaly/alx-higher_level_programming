#!/usr/bin/python3
""" This module is about a function to prints a square."""


def print_square(size):
    """Args: size must be an integers
       Return void, prints a square with '#'
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print()
