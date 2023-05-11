#!/usr/bin/python3

""" Rotate 2D Matrix 90 Degrees Clockwise"""


def rotate_2d_matrix(matrix):
    """ Function for rotating 2D Matrix
    Given an n x n 2D matrix,
    - Do not return anything.
    """

    m = len(matrix[0])

    for i in range(m - 1, -1, -1):
        for k in range(0, m):
            matrix[k].append(matrix[i].pop(0))
