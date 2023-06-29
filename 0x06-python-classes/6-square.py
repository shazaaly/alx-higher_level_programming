#!/usr/bin/python3
"""    This script defines a basic Square class."""


class Square:
    """
    Define a class named Square
    Attributes:
    __size : private
    """

    def __init__(self, __position=(0, 0), __size=0):
        """Intializing the square object with a private size attribute
        Args :
        __size : size of squre
        """
        self.__position = __position
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
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ",  end="")
                print("#" * (self.__size))




    @property
    def position(self):
        """a method to access postition
        Args:
            self
        Returns: position tuple"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or \
            len(value) != 2 or \
                not all(isinstance(v, int) and v >= 0 for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
