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
        print(x)
        if n%x==0:
            print(x*x!=n)
            if x*x!=n: i+=2
            else: i+=1
            print(i)
            # i+=2 if x*x != n else 1
    return i

# print(divisible_triangle_number(167))
print(factors(6))