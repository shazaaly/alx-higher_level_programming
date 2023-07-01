#!/usr/bin/python3
""" This module is about a function to divide matrix elements"""


def matrix_divided(matrix, div):
    """
     function that divides all elements of a matrix
     Args: matrix and a div: number to be divide on or none
     Returns : a new matrix, elements rounded to 2 decimal places or matrix if div == None
    """
    if div is None:
        return matrix
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if matrix == [] or not (isinstance(matrix, list)) or \
        not all(isinstance(row, list) for row in matrix) or \
        not all(isinstance(elem, (int, float)) for row
                in matrix for elem in row):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return new_matrix
