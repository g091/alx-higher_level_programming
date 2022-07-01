#!/usr/bin/python3
""" Module that divides elements of a matrix"""


def matrix_divided(matrix, div):
    """ Divides a matrix by the div"""

    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/float")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")

        for member in row:
            if not isinstance(member, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")

    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]

    return new_matrix
