#!/usr/bin/python3
"""Module def pascal_triangle(n): that returns a
list of lists of integers representing the
Pascal’s triangle of n:"""


def pascal_triangle(n=5):
    """Implements the pascal's triangle"""
    pscl = [[0]*i for i in range(1, n+1)]
    for i in range(n):
        pscl[i][0] = 1
        pscl[i][-1] = 1
        for j in range(0, i//2):
            pscl[i][j+1] = pscl[i-1][j] + pscl[i-1][j+1]
            pscl[i][i-j-1] = pscl[i-1][j] + pscl[i-1][j+1]

    return pscl
