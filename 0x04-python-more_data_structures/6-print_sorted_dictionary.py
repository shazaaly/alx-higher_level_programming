#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if not a_dictionary:
        return
    sorted_list = sorted(a_dictionary.keys())
    for key in sorted_list:
        value = a_dictionary[key]
        print(key, value)
    return sorted_list
