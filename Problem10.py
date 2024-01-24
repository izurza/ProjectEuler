## Problem 10
from Problem7 import find_next_prime

def primeSummation(n):
    primes = [2,3]
    while True:
        next = find_next_prime(primes[-1])
        if next>n: break
        primes.append(next)
    return sum(primes)