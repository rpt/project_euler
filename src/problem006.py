#!/usr/bin/env python3

# Problem 6:
#     The sum of the squares of the first ten natural numbers is,
#         1^2 + 2^2 + ... + 10^2 = 385
#     The square of the sum of the first ten natural numbers is,
#         (1 + 2 + ... + 10)^2 = 55^2 = 3025
#     Hence the difference between the sum of the squares of the first ten
#     natural numbers and the square of the sum is 3025 - 385 = 2640.
#     Find the difference between the sum of the squares of the first one
#     hundred natural numbers and the square of the sum.
# Answer:
#     25164150

def problem6(n):
    sum_of_squares = int((2 * n + 1) * (n + 1) * n / 6)
    just_sum = int((n + 1) * n / 2)
    return just_sum * just_sum - sum_of_squares

# print(problem6(100))

def problem6n(n):
    '''Quick, naive implementation.'''
    sum_of_squares = 0
    just_sum = 0
    for i in range(1, n + 1):
        sum_of_squares += i * i
        just_sum += i

    return just_sum * just_sum - sum_of_squares
