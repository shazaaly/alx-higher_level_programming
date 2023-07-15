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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Args:
            list_objs (_list_):a list of instances who inherits of Base.
        Returns:
            void: write json to a file
        """
        target_file = cls.__name__ + ".json"
        list_of_dicts = []
        with open(target_file, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                for obj in list_objs:
                    dic = obj.to_dictionary()
                    list_of_dicts.append(dic)
                file.write(cls.to_json_string(list_of_dicts))

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
