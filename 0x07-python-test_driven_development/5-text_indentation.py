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
    # remove spaces at bothends
    # split at \n into lines
    # strip the separated lines
    # manage spaces

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_marks = ['.', '?', ':']
    lines = []
    current_line = ''

    for char in text:
        current_line += char

        if char in punctuation_marks:
            lines.append(current_line.strip())
            lines.append('\n')
            lines.append('\n')
            current_line = ''

    lines.append(current_line.strip())

    print(''.join(lines))
