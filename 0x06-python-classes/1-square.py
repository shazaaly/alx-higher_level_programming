#!/usr/bin/python3
"""    This script defines a basic Square class."""


class Square:
    """
    Define a class named Square
    Attributes:
    __size : private
    """

    def __init__(self, __size):
        """Intializing the square object with a private size attribute
        Args :
        __size : size of squre
        """

        self.__size = __size
