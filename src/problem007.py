#!/usr/bin/env python3

# Problem 7:
#     By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
#     see that the 6th prime is 13.
#     What is the 10 001st prime number?
# Answer:
#     104743

from math import sqrt, floor

def is_prime(x):
    '''Primality check.'''
    if x == 1:
        return False
    if x < 4:
        return True
    if (x % 2) == 0:
        return False
    if x < 9:
        return True
    if (x % 3) == 0:
        return False

    for i in range(5, floor(sqrt(x)) + 1, 6):
        if (x % i) == 0 or (x % (i + 2)) == 0:
            return False
    return True

def problem7(x):
    if x == 1:
        return 2
    if x == 2:
        return 3

    counter = 2
    i = 5
    while True:
        if is_prime(i):
            counter += 1
            if counter == x:
                return i
        if is_prime(i + 2):
            counter += 1
            if counter == x:
                return i + 2
        i += 6

# print(problem7(10001))
