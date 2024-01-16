## Problem 2
def fiboEvenSum(n):
    previous, current = 0, 1
    sum = 0
    if (n<=1):
        return 0
    while (current<n):
        previous, current = current, previous + current
        if (current%2==0):
            sum += current
    return sum