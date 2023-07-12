#!/usr/bin/python3

"""writes a string to a text file (UTF8) and
returns the number of characters
"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)
    Args:
       filename (str, optional).
       text (str, optional).
    Returns :number of characters written
    """
    # check file presence
    # if exists overwrite it
    # ifelse create file

    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        count = len(content)
        return count
