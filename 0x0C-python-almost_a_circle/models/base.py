#!/usr/bin/python3

"""This module is to manage id attribute in all future classes
"""


class Base:
    """class to handle id attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """cass constructor
        Args:
           id (int)
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
