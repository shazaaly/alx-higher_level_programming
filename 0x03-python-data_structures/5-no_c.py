#!/usr/bin/python3
def no_c(my_string):
    if not my_string:
        return ("")
    else:
        new_str = ""
        for char in my_string:
            if char != 'c' and char != 'C':
                new_str += char
        return (new_str)
