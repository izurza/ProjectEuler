## Problem 9
import math

def specialPyrhagoreanTriplet(n):
    for x in range(1,n):
        for y in range(x,n):
            zsqr = x**2+y**2
            z = math.sqrt(zsqr)
            if(z%1==0 and x+y+z==n):
                return x*y*z