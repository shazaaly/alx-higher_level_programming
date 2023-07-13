#!/usr/bin/python3
"""Module to a list of lists of integers representingthe Pascals triangle of n:
"""


def pascal_triangle(n):
    """returns a list of lists of integers
       representing the Pascal triangle of n
    Args: n (int)
    """

    tri = []

    for row in range(n):
        row_list = []
        row[0] = 1
        row[len(row) - 1] = 1
        for el in row:
            if row >= 2:
                el = row - 1[0] + row - 1[1]
                row_list.append(el)
        for j in range(row):
            if j > 1:
                row[j] = row - 1[j - 1] + row - 1[j]
                row_list.append(row[j])

    tri.append(row_list)
