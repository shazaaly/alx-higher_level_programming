#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    else:
        print("{:d}".format(my_list[len(my_list) - 1]))
        print_reversed_list_integer(my_list[:-1])
