#!/usr/bin/python3
''' A module that rotates a matrix by 90 degrees
'''


def rotate_2d_matrix(matrix):
    ''' Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    '''
    n = len(matrix)

    for i in range(n):
        j = i
        while j < n:
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
            j += 1

    for i in range(n):
        p1, p2 = 0, len(matrix[i]) - 1
        temp = matrix[i][p1]
        matrix[i][p1] = matrix[i][p2]
        matrix[i][p2] = temp
