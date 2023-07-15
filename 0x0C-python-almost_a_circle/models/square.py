#!/usr/bin/python3

"""This module is about a class Square that inherits from Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle
    Args:
       Rectangle (_type_): id, size, x, y
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor method"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, val):
        """size setter"""
        if type(val) != int:
            raise TypeError("size must be an integer")
        if val < 0:
            raise ValueError("size must be greater than zero!")
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        if args and len(args) != 0:
            for arg in args:
                if len(args) >= 1:
                    self.id = args[0]
                if len(args) >= 2:
                    self.size = args[1]
                if len(args) >= 3:
                    self.x = args[2]
                if len(args) >= 3:
                    self.x = args[2]
        else:
            for k, v in kwargs.items():
                return (k, v)

    def __str__(self):
        """_summary_

        Returns:
            string representation [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return f"[Square]\
 ({self.id})  {self.x}/{self.y} - {self.width}"
