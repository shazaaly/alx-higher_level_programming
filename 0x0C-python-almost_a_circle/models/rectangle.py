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
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be greater than zero!")
        self.__width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be greater than zero!")
        self.__height = height

        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be greater than zero!")
        self.__x = x

        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be greater than zero!")
        self.__y = y

    def area(self):
        """function to calc area of rectangle

        Returns:
            int: area
        """
        return self.__width * self.__height

    def display(self):
        """display rectangle with "#"

        Returns:
           print "#" according to w and h_
        """

        for y_val in range(self.__y):
            print()

        for i in range(self.__height):
            for x_val in range(self.__x):
                print(" ", end="")
            print("#" * self.__width)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute
        """
        if args and len(args) != 0:

            for arg in args:

                if len(args) >= 1:
                    self.id = args[0]
                if len(args) >= 2:
                    self.width = args[1]
                if len(args) >= 3:
                    self.height = args[2]
                if len(args) >= 4:
                    self.x = args[3]
                if len(args) >= 5:
                    self.y = args[4]
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def __str__(self):
        """_summary_

        Returns:
            string representation [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return f"[Rectangle]\
 ({self.id}){self.__x}/{self.__y} - {self.__width}/{self.__height}"

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

    def to_dictionary(self):
        """dictionary representation """
        return {
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,

        }
