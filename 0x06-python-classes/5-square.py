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

    def area(self):
        """A public instance method to calculate area of square
        Returns : square area"""
        return self.__size ** 2

    @property
    def size(self):
        """Returns : size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """propery setter for size
        Args : value
        Raises: Type
        error or value error"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)
