#!/usr/bin/python3
from functools import reduce


def uniq_add(my_list=[]):
    my_set = set(my_list)
    total = reduce(lambda x, y: x + y, my_set)
    return total
