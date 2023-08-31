#!/usr/bin/python3
''' Island perimeter computing module.
'''


def island_perimeter(grid):
    '''
    Returns the perimeter of the island described in grid with no lakes.
    '''

    n = len(grid)
    l_index = -1
    b_index = -1
    l = 0
    b = 1
    for row in range(n):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                if l_index != -1:
                    if l_index == col:
                        l += 1
                else:
                    l = 1
                l_index = col

            if grid[row][col] == 1 and grid[row + 1][col] == 0:
                if grid[row][col + 1] == 1:
                    if b_index == -1:
                        b = 1
                    else:
                        if b_index == row:
                            b += 1
                    b_index = row
                elif grid[row][col] == 1:
                    b += 1

    if l == b:
        return (4 * l)
    elif l > b or b > l:
        sides = l + b
        return (2 * sides)
