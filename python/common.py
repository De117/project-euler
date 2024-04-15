import math, itertools
from collections import Counter
from functools import reduce
from typing import Union, Dict, Iterable, List, Iterator


def sieve_segmented(upper_bound=math.inf, segment_size=1048576) -> Iterator[int]:
    """Sieve of Erastothenes, segmented version.

    Unlike the plain sieve, it reuses a fixed-size memory chunk for sieving.
    Uses O(π(upper_bound)) memory.

    Returns primes under `upper_bound`.
    """

    table = [0] * segment_size
    table[0] = table[1] = 1  # Mark off 0 and 1

    known_primes = {}

    i_segment = 0
    while True:
        segment_base = i_segment * segment_size
        segment_top = (i_segment + 1) * segment_size

        if segment_base >= upper_bound:
            break

        if segment_top > upper_bound:  # Clip last segment to fit
            segment_top = upper_bound


        # Mark of all multiples of known primes
        for p, next_multiple in known_primes.items():
            i = next_multiple
            while i < segment_top:
                table[i - segment_base] = 1
                i += p

            known_primes[p] = i


        # Proceed with standard algorithm
        try:    prime = prime
        except: prime = 1

        while True:
            # 1. get first prime in block
            next_prime = max(prime + 1, segment_base)
            while next_prime < segment_top and table[next_prime - segment_base]:
                next_prime += 1
            prime = next_prime

            # (Is it really in the block? If no, there are no primes left in it.)
            if prime == segment_top:
                break
            # Also, are we over the bound? Then we're already done.
            if prime >= upper_bound:
                break

            # 2. mark off its multiples
            i = prime * prime
            while i < segment_top:
                table[i - segment_base] = 1
                i += prime
            known_primes[prime] = i

            yield prime

        # Clear table before next iteration
        for i in range(len(table)):
            table[i] = 0

        i_segment += 1

# Construct a memoized iterator through all primes.
_primes_iterator = sieve_segmented()
_primes_cache = [next(_primes_iterator)]

def primes(N=math.inf):
    """Return first N primes"""

    if N == math.inf:
        # Fast lane for PyPy
        yield from _primes_cache
        while True:
            prime = next(_primes_iterator)
            _primes_cache.append(prime)
            yield prime
    else:
        yield from itertools.islice(_primes_cache, min(N, len(_primes_cache)))
        i = len(_primes_cache)
        while i < N:
            prime = next(_primes_iterator)
            _primes_cache.append(prime)
            yield prime
            i += 1


def is_prime(N: int):
    if N <= 1: return False
    elif N <= 3: return True
    elif N % 2 == 0: return False

    upper_bound = math.ceil(N**0.5)

    for i in range(3, upper_bound+1, 2):
        if N % i == 0:
            return False
    return True


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

        for prime in primes():
            if N == 1:
                break

            modified = False
            while N % prime == 0:
                self.coefficients[prime] += 1
                N //= prime
                modified = True

            # For numbers with a large prime factor p₁, it takes a while
            # to go through (=generate) all the primes ≤ p₁ checking for
            # divisibility. It's faster to check directly (when applicable).
            #
            if modified and is_prime(N):
                self.coefficients[N] += 1
                break


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


def euler_phi(n: int) -> int:
    """Number of positive integers coprime to n."""
    # Euler's totient function is a multiplicative function. That is,
    #
    #   φ(m*n) = φ(m)*φ(n) if m and n are relatively prime.
    #
    # Every number n can be decomposed to a product of powers of primes p_1...p_r,
    # so
    #   φ(n) = φ(p_1^k_1)  * ... * φ(p_r^k_r)
    #        = φ(p_1)^k_1  * ... * φ(p_r)^k_r
    #        = (p_1-1)^k_1 * ... * (p_r-1)^k_r
    #
    # For more, see: https://en.wikipedia.org/wiki/Euler%27s_totient_function
    return product(p**(k-1) * (p-1) for p, k in PrimeDecomposition(n).coefficients.items())
