#!/usr/bin/env python3

# Problem 1:
#     If we list all the natural numbers below 10 that are multiples of 3 or 5,
#     we get 3, 5, 6 and 9. The sum of these multiples is 23.
#     Find the sum of all the multiples of 3 or 5 below 1000.
# Answer:
#     233168

def problem1(n):
    def sumd(x, n):
        k = (n - 1) // x
        return x * k * (k + 1) // 2

    return sumd(3, n) + sumd(5, n) - sumd(15, n)

# print(problem1(1000))

def problem1n(n):
    '''Naive, slow version.'''
    c = 0
    for i in range(1, n):
        if (i % 3 == 0) or (i % 5 == 0):
            c += i
    return c
