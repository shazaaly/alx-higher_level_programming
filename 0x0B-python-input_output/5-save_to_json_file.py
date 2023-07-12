#!/usr/bin/python3

"""a function that writes an Object to a text file,
using a JSON representation:
"""

import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file,
    using a JSON representation:
    Args:
    my_obj (_type_)
    """

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
