## Problem 12
import math
def divisible_triangle_number(n):
    i=1
    while(True):
        tri = triangle_number(i)
        if factors(tri)>=n:
            return tri
        i+=1

def triangle_number(n):
    return sum(range(n+1))

def factors(n):
    i=0
    for x in range(1,int(math.sqrt(n))+1):
        if n%x==0:
           i+=2 if x*x != n else 1
    return i