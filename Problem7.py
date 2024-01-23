def nthPrime(n):
    primes = [2]
    number = 3
    while(len(primes)<n):
        is_prime = True
        for div in range(2, int(number ** 0.5) + 1):
            if number % div == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
        number += 2
    print(primes)
    return primes[-1]

print(nthPrime(10001))