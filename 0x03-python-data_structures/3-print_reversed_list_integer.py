#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 0:
        return
    else:
        print(my_list[len(my_list) - 1])
        print_reversed_list_integer(my_list[:-1])
