#!/usr/bin/python3
"""
Module for class that inherits from REctangle
"""

"""Parent class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Basic class Square that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size must be private. No getter or setter, must be a positive
            integer, validated by integer_validator
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Return the area of the rectangle."""
        return self.__size * self.__size

    def __str__(self):
        """resturns description of sqaure like [Square] <width>/<height>"""
        desc = type(self).__name__
        desc += str(self.__size) + "/" + str(self.__size)
        return desc
