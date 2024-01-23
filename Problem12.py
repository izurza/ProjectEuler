
def divisible_triangle_number(n):
    i=1
    while(True):
        if factors(triangle_number(i))>=n:
            return triangle_number(i)
        i+=1


def triangle_number(n):
    return sum(range(n+1))
def factors(n):
    i=0
    for x in range(1,n+1):
        if n%x==0:
            i+=1
    return i

print(divisible_triangle_number(167))