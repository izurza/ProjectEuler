import math

def find_next_prime(n):
    while True:
        prime = True
        n += 2
        for div in range(2, int(math.sqrt(n))+1):
            if n % div == 0:
                prime = False
                break
        if prime:
            return n

def nthPrime(n):
    primes = [2,3]
    while(len(primes)<n):
        primes.append(find_next_prime(primes[-1]))
    return primes[-1]
