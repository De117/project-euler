from math import ceil
from functools import reduce
from collections import Counter

def isprime(n):
    """Is n prime?"""
    if n == 2:
        return True

    for i in range(2, ceil(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def calc_arity(n, factor):
    """How many times is n divisible by factor?"""
    exp = 0
    while int(n % factor**(exp+1)) == 0:
        exp += 1
    return exp


def factorize(n):
    """Factorize n into its prime factors"""
    if isprime(n):
        return [(n,1)]

    prime_factors = []
    for factor in range(2, ceil(n/2)+1):
        if n % factor == 0 and isprime(factor):
            prime_factors.append((factor, calc_arity(n, factor)))
    return prime_factors


def add_decompositions(decomp1, decomp2):
    """Add two prime-factor decompositions by max(arity1, arity2) for each factor."""
    result = []

    d1 = Counter(dict(decomp1))
    d2 = Counter(dict(decomp2))

    for factor in set(d1).union(set(d2)):
        result.append( (factor, max(d1[factor], d2[factor])) )

    return result


if __name__ == "__main__":
    N = 20
    decompositions = [factorize(i) for i in range(2, N + 1)]

    added = reduce(lambda d1, d2: add_decompositions(d1, d2), decompositions)

    product = 1
    for factor, power in added:
        product *= factor ** power

    print(f"The smallest number evenly divisible by 1 to {N} is {product}")
