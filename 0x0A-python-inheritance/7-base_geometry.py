#!/usr/bin/python3
"""
Module for basic class implementation
"""


class BaseGeometry:
    """Basic class named BaseGeometry
    """

    def area(self):
        """
        Public instance method: raises exception
        No implementation yet
        Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        public instance method: validate value
        Args :
            name and value
        Raises :
            if value is not an integer: TypeError exception,
            with the message <name> must be an integer
            if value is less or equal to 0: raise a ValueError
            exception with the message <name> must be greater than 0
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
