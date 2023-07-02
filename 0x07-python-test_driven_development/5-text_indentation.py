#!/usr/bin/python3
""" This module is about a function
function that prints a text with 2 new lines
after each of these characters: ., ? and :"""


def text_indentation(text):
    """
     function that prints a text with 2 new lines after ., ? and :
     Args: text string
     Returns : void, prints text indented
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""

    for char in text:
        if char in [".", "?", ":"]:
            result += char + "\n\n"
        else:
            result += char

    lines = []

    for line in result.splitlines():
        lines.append(line.strip())
    result = "\n".join(lines)

    print(result)
