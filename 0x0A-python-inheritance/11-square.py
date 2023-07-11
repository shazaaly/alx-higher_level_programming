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
        self.integer_validator("size", size)  # valid
        super().__init__(size, size)    # Call the parent's constructor with \
        # width and height set to size
        self.__size = size
