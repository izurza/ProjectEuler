## Problem 25

def digit_fibonacci(n):
    index=1
    previous, current = 0, 1
    if (n<=1):
        return index
    while (len(str(current))<n):
        previous, current = current, previous + current
        index += 1
    return index