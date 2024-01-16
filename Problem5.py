## Problem 5
def smallestMult(n):
    res=1
    for x in range(1, n+1):
        res = lcm(res,x)
    return res 

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def lcm(a,b):
    return a*b//gcd(a,b)