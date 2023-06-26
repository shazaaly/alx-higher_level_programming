#!/usr/bin/python3
def safe_print_integer(value):
    try:
        int_value = int(value)
        print("{}".format(int_value), end="")
        print()
        return True
    except ValueError:
        return False
