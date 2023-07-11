#!/usr/bin/python3
"""This module is Write a class MyList that inherits from list,
contains a afunction prints the list, but sorted (ascending sort)
"""


class MyList(list):
    """
    Define a class named MyList
    Inherits from: list
    has Public instance method: def print_sorted(self)

    Examples:
    >>> import doctest
    >>> doctest.testfile('1-my_list.txt')
    """
# self: reference to the instance of the MyList class.
    def print_sorted(self):
        """method takes self as arg
        Args: self
        Returns : void : print sorted list"""
        new_list = sorted(self)
        print(new_list)
