import math, itertools
from collections import Counter
from functools import reduce
from typing import Union, Dict, Iterable

def is_prime(N: int):
    if N <= 1: return False
    elif N <= 3: return True
    elif N % 2 == 0: return False

    upper_bound = math.ceil(N**0.5)

    for i in range(3, upper_bound+1, 2):
        if N % i == 0:
            return False
    return True


def primes(N=math.inf):
    """Generate first N primes"""
    if N <= 0: return
    elif N == 1: yield 2;
    elif N == 2: yield 2; yield 3; return
    else: yield 2; yield 3

    i = 3
    last_prime = 3

    while i <= N:
        candidate = last_prime + 2
        while not is_prime(candidate):
            candidate += 2
        yield candidate
        last_prime = candidate
        i += 1


def product(l: Iterable):
    """Product of numbers in given iterable"""
    return reduce(lambda a,b: a*b, l, 1)


class PrimeDecomposition:
    """A natural number as its prime decomposition."""

    def __init__(self, N_or_coefficients: Union[int, Dict[int, int]]):

        if isinstance(N_or_coefficients, dict):
            self.coefficients = Counter(N_or_coefficients)
            self.N = product(k**v for k,v in self.coefficients.items())
            return

        assert isinstance(N_or_coefficients, int)
        N = N_or_coefficients
        assert N >= 1
        self.N = N
        self.coefficients = Counter()

        if is_prime(N):
            self.coefficients[N] = 1
            return

        for prime in primes():  # all primes
            if N == 1:
                break

            while N % prime == 0:
                self.coefficients[prime] += 1
                N //= prime


    def __eq__(self, other: "PrimeDecomposition"):
        return self.N == other.N and self.coefficients == other.coefficients


    def __and__(self, other: "PrimeDecomposition"):
        return PrimeDecomposition(self.coefficients & other.coefficients)


    def __or__(self, other: "PrimeDecomposition"):
        return PrimeDecomposition(self.coefficients | other.coefficients)


    def __repr__(self):
        return f"PrimeDecomposition({self.N})"


    def get_proper_divisors(self):
        """Calculate the proper divisors of this number"""

        def power_range(base, exponent_stop):
            return [base**i for i in range(exponent_stop)]

        if not self.coefficients:
            return []
        elif len(self.coefficients) == 1:
            prime, coef = next(iter(self.coefficients.items()))
            return power_range(prime, coef)

        # Take all prime-only divisors
        factors = [power_range(prime, coef+1) for (prime, coef) in self.coefficients.items()]
        # Multiply all combinations (cartesian product) to get all divisors
        divisors = [product(e) for e in itertools.product(*factors)]
        # Proper divisors are all (positive) divisors except the number itself
        return sorted(divisors)[:-1]
