## Problem 3
def largesPrimeFactor(n):
    prime = 2
    largest = 1

    while(prime<=n):
        if (n%prime==0):
            largest = prime
            n//=prime
        else:
            prime+=1
    return largest