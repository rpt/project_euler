#!/usr/bin/env python3

# Problem 4:
#     A palindromic number reads the same both ways. The largest palindrome
#     made from the product of two 2-digit numbers is 9009 = 91 x 99.
#     Find the largest palindrome made from the product of two 3-digit numbers.
# Answer:
#     906609

from math import ceil

def problem4():
    def is_palindrom(x):
        s = str(x)
        if s == s[::-1]:
            return True
        return False

    answers = [0]
    for i in range(999, 99, -1):
        for j in range(i - 1, 99, -1):
            x = i * j
            if x < max(answers):
                break
            if is_palindrom(x):
                answers.append(x)
    return max(answers)

# print(problem4())
