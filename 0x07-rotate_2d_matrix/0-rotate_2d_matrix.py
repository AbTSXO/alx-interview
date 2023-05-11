#!/usr/bin/python3
'''2D matrix'''

def rotate_2d_matrix(matrix):
    '''rotates a 2d matrix 
    Returns: none'''
    l, r = 0, len(matrix) - 1

    while l < r:
        for i in range(r - l):
            t, b = l, r
            topLeft = matrix[t][l + i]
            matrix[t][l + i] = matrix[b - i][l]
            matrix[b - i][l] = matrix[b][r - i]
            matrix[b][r - i] = matrix[t + i][r]
            matrix[t + i][r] = topLeft
        r -= 1
        l += 1
