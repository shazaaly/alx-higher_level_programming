#!/usr/bin/python3


def pascal_triangle(n):
    """returns a list of lists of integers
       representing the Pascal triangle of n
    Args: n (int)
    """

    for row in n:
        for col in row:
            row[0] = 1
            row[len(row) - 1] = 1

