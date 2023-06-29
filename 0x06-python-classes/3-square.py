#!/usr/bin/python3
"""    This script defines a basic Square class."""


class Square:
    """
    Define a class named Square
    Attributes:
    __size : private
    """

    def __init__(self, __size=0):
        """Intializing the square object with a private size attribute
        Args :
        __size : size of squre
        """
        self.__size = __size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = __size

    @property
    def area(self):
        """A public instance method to calculate area of square"""
        return self.__size * 2
