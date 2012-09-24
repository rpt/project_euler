#!/usr/bin/env python3

# Problem 10:
#     The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#     Find the sum of all the primes below two million.
# Answer:
#     142913828922
# Notes:
#     - Using the Sieve of Eratosthenes

def eratosthenes(n):
    '''Sieve of Eratosthenes.'''
    def nextp(p, numbers):
        while numbers[p] == 0:
            p += 2
        return p
        
    primes = [2]
    numbers = {i : 1 for i in range(3, n + 2, 2)}

    p = 3
    while p < n:
        for i in range(p, n, p):
            numbers[i] = 0

        primes.append(p)
        p = nextp(p, numbers)

    return primes

def problem10(n):
    return sum(eratosthenes(n))

# print(problem10(2000000))
