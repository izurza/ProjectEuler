## Problem 20
import math

def sum_factorial_digits(n):
    return sum([int(x) for x in str(math.factorial(n))])

