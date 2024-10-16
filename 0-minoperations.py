#!/usr/bin/python3
"""
a method that calculates the fewest number of operations
needed to result in exactly n H characters
"""


def minOperations(n):
    if n <= 1:
        return 0
    """no operations needed for n=1
    or n=0
    """
    operations = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    return operations
