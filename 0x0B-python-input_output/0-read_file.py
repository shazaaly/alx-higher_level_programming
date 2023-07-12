#!usr/bin/python3
"""This Module is about reading eads a text file (UTF8)
 and prints it to stdout
"""


def read_file(filename=""):
    """read files
    Args:
        filename (str, optional)
    """

    with open(filename, "r") as file:
        content = file.read()
        print(content)
