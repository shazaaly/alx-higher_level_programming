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

    lines = text.strip().split("\n")
    is_space = False
    result = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        ind_line = []
        is_space = False
        result = []

        for i, char in enumerate(line):
            if char in [".", ":", "?"]:
                ind_line.append(char)
                if i < len(line) - 1:
                    ind_line.append("\n\n")
                is_space = False

            elif char == " ":
                if not is_space:
                    ind_line.append(char)
                    is_space = True
            else:
                ind_line.append(char)
                is_space = False

        result.extend(ind_line)

    result = "\n".join(result)
    print(result)
