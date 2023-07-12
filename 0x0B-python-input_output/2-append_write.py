#!/usr/bin/python3

"""function that appends a string at the end of a text file
(UTF8) and returns the number of characters added
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file
      (UTF8) and returns the number of characters added
    Args:
       filename (str, optional).
       text (str, optional).
    """

    with open(filename, "a", encoding="utf-8") as file:
        file.write("\n" + text)

    with open(filename, "r") as file:
        file.seek(0, 2)
        count = file.tell()
        return count
