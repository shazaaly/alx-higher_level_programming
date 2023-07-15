#!/usr/bin/python3

"""This module is to manage id attribute in all future classes
"""

import json


class Base:
    """class to handle id attribute
    """
    __nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

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
