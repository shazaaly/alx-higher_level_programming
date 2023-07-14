#!/usr/bin/python3

"""This module is about a class Rectangle that inherits from Base
"""

from models.base import Base


class Rectangle(Base):
    """class with private attributes
    Args: width, height, x, y
    Raises : TypeError, ValueError
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ constructor to set attributes upon instantiation"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, val):
        """width setter"""
        if type(val) != int:
            raise TypeError("width must be an integer")
        if val < 0:
            raise ValueError("width must be greater than zero!")
        self.__width = val

    """height attribute"""
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        if type(val) != int:
            raise TypeError("height must be an integer")
        if val < 0:
            raise ValueError("height must be greater than zero!")

        self.__height = val

    """x attribute"""
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        if type(val) != int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be greater than zero!")

        self.__x = val

    """y attribute"""
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        if type(val) != int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be greater than zero!")
        self.__y = val
