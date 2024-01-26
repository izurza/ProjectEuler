## Problem 6
def sumSquareDifference(n):
    L = list(range(1,n+1))
    squares = [x**2 for x in L]
    return sum(L)**2-sum(squares)

