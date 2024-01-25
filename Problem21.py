## Problem 20

def sum_amicable_num(n):
    an = []
    for x in range(4,n+1):
        a=x
        b = sum(factors(x))
        if a == sum(factors(b)) and a!=b: an.append(a)
    return sum(an)

def factors(n):
    factors = []
    for x in range(1,n//2+1):
        if n%x==0:
           factors.append(x)
    return factors