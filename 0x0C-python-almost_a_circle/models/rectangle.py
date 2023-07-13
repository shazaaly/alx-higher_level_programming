#!/usr/bin/python3

"""This module is about a class Rectangle that inherits from Base
"""

Base = __import__("base.by").Base


class Rectangle(Base):
    """class with private attributes :width, height, x, y
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
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    """height attribute"""
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    """x attribute"""
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    """y attribute"""
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
