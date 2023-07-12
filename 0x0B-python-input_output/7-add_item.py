#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
import os


if __name__ == "__main__":

    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    if os.path.isfile("add_item.json"):
        items = load_from_json_file("add_item.json")
    else:
        items = []

    save_to_json_file(items + sys.argv[1:], "add_item.json")
