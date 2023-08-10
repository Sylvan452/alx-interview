#!/usr/bin/python3
"""
A module defines a function that calculates the fewestnumber of 
operations needed to result in exactly n H characters in the a given file
"""


def minOperations(n):
    """
    This returns the fewest number of operations needed to result in 
    exactly n H characters in a given file.
    """
    if type(n) is not int or n <= 1:
        return 0
    summation = []
    factor = 2
    while (n % factor) is 0 and (n // factor) is not 1:
        summation.append(factor)
        n = n //factor 
    factor = 3
    while n > factor:
        while (n % factor) is 0 and (n // factor) is not 1:
            summation.append(factor)
            n = n //factor 
        factor += 2
    summation.append(n)
    return sum(summation)
