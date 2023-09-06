#!/usr/bin/python3


def find_first_prime(numbers):
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    for num in numbers:
        if is_prime(num):
            return num
    return 0


def isWinner(x, nums):
    '''
    '''
    p = 1

    def find_multiples(number, n):
        multiples = set()
        for i in range(1, n + 1):
            multiple = number * i
            if multiple <= n:
                multiples.add(multiple)
            else:
                break
        return multiples

    winner = None
    ben = 0
    maria = 0
    round = 1

    for n in nums:
        ints = set(range(1, n + 1))
        while p != 0:
            p = find_first_prime(ints)
            multiples = find_multiples(p, n)

            ints = ints - multiples

            if p == 0:
                if round % 2 == 0:
                    winner = 'maria'
                    maria += 1
                else:
                    winner = 'ben'
                    ben += 1

            round += 1

    if maria > ben:
        return 'Ben'
    else:
        return 'Maria'
