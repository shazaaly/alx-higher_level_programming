#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 0 or not my_list:
        return
    else:
        print("{:d}".format(my_list[len(my_list) - 1]))
        print_reversed_list_integer(my_list[:-1])
