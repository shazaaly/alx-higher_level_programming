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

    words = text.split()
    text = " ".join(words)

    text = text.replace('.', ".\n\n")
    text = text.replace('?', "?\n\n")
    text = text.replace(':', ":\n\n")
    text = text.strip()

    print(text)
