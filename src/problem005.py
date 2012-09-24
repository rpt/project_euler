#!/usr/bin/env python3

# Problem 5:
#     2520 is the smallest number that can be divided by each of the numbers
#     from 1 to 10 without any remainder.
#     What is the smallest positive number that is evenly divisible by all of
#     the numbers from 1 to 20?
# Answer:
#     232792560

from problem010 import eratosthenes

def mul(list):
    '''Helper function to compute the product of the elements on the list.'''
    prod = 1
    for i in list:
        prod *= i
    return prod

def problem5(n):
    def red(x, list):
        for i in list:
            if (x % i) == 0:
                x /= i
        return int(x)

    primes = eratosthenes(n + 1)
    rest = []
    for i in range(4, 21):
        if i not in primes:
            rest.append(red(i, primes + rest))
    
    return mul(primes + rest)

# print(problem5(20))
