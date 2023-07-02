#!/usr/bin/python3
"""Defines a function that generate pascals triangle.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascals triangle of n:
    """
    # Create a new triangle
    triangle = []

    if (n <= 0):
        return []

    for row in range(n):
        # new row in the triangle
        current_row = []
        for col in range(row + 1):
            if col == 0 or col == row:
                value = 1
            else:
                value = triangle[row - 1][col - 1] + triangle[row - 1][col]
            current_row.append(value)
        triangle.append(current_row)

    return triangle
