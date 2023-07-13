#!/usr/bin/python3
"""Module to a list of lists of integers representingthe Pascals triangle of n:
"""


def pascal_triangle(n):
    """returns a list of lists of integers
       representing the Pascal triangle of n
    Args: n ()
    """

    tri = [[1]]

    for row in range(n):
        row_list = []
        row[0] = 1
        row[len(row) - 1] = 1
        for col in range(row):
            if row >= 2:
                tri[row].append([row - 1][col - 1] + [row - 1][col])

    return tri
