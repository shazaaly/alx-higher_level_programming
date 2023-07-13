#!/usr/bin/python3
"""Module to a list of lists of integers representingthe Pascals triangle of n:
"""


def pascal_triangle(n):
    """returns a list of lists of integers
       representing the Pascal triangle of n
    Args: n ()
    """

    tri = []

    for row in range(n):
        curr_row = []
        for col in range(row + 1):
            if col == 0 or col == row:
                curr_row.append(1)
            else:
                curr_row.append(tri[row - 1][col - 1] + tri[row - 1][col])
        tri.app(curr_row)
    return tri
