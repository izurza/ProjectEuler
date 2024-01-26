## Problem 16
def power_digit_sum(n):
    return sum(int(x) for x in str(2**n))