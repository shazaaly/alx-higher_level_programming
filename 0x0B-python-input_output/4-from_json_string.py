#!/usr/bin/python3

"""unction that returns an object
(Python data structure) represented by a JSON string
"""

import json


def from_json_string(my_str):
    """function that returns an object represented by a JSON string
    Args:
        my_str (_type_)
    """

    return json.loads(my_str)
