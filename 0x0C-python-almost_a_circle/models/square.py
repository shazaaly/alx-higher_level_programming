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

    def __str__(self):
        """_summary_

        Returns:
            string representation [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return f"[Square]\
 ({self.id})  {self.x}/{self.y} - {self.width}/{self.width}"
