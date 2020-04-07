from math import ceil

def isprime(n):
    if n == 2:
        return True

    for i in range(2, ceil(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def factorize(n):
    prime_factors = []
    for i in range(2, ceil(n**0.5)):
        if n%i==0 and isprime(i):
            prime_factors.append(i)
    return prime_factors

n = 600851475143
print(factorize(n))
