#!/usr/bin/env python3

# Problem 3:
#     The prime factors of 13195 are 5, 7, 13 and 29.
#     What is the largest prime factor of the number 600851475143 ?
# Answer:
#     6857
# Notes:
#     - Using the Fermat's factorization method

from math import sqrt, ceil

def fermat(x):
    '''Fermat's factorization.'''
    def is_square(b):
        return (sqrt(b) % 1) == 0

    a = ceil(sqrt(x))
    b2 = a * a - x
    while (not is_square(b2)) and a*a - b2 < x:
        b2 += 2 * a + 1
        a += 1

    if is_square(b2):
        b = sqrt(b2)
        return (int(a - b), int(a + b))
    else:
        return (1, x)

def problem3(x):
    def do_find(x):
        (small, large) = fermat(x)
        if small == 1:
            return large
        else:
            return max(do_find(small), do_find(large))
    
    return do_find(x)

# print(problem3(600851475143))
