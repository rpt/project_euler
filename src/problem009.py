#!/usr/bin/env python3

# Problem 9:
#     A Pythagorean triplet is a set of three natural numbers, a < b < c,
#     for which,
#         a^2 + b^2 = c^2
#     For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#     There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#     Find the product abc.
# Answer:
#     31875000 (200, 375, 425)

def problem9(s):
    '''Slow, naive implementation.'''
    for a in range(3, s / 2, 3):
        for b in range(4, s / 2, 2):
            c = s - a - b
            if a*a + b*b == c*c:
                return a * b * c
    return -1

print(problem9(1000))
