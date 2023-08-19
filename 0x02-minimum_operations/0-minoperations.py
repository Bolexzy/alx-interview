#!/usr/bin/python3
'''The minimum operations coding challenge.
    Available operations:
        copy
        paste
'''


def minOperations(n):
    ''' Given a number n, write a method that calculates the
    fewest number of operations needed to result
    in exactly n H characters in the file.
    '''

    min_ops = 0

    if n <= 1:
        return min_ops

    for i in range(2, n + n):
        while n % i == 0:
            min_ops += i
            n /= i

        if n == 1:
            return min_ops
