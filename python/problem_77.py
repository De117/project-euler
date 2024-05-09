# Problem 77 (Prime Summations)
# =============================
#
# It is possible to write ten as the sum of primes in exactly five different ways:
#
#     7+3
#     5+5
#     5+3+2
#     3+3+2+2
#     2+2+2+2+2
#
# What is the first value which can be written as the sum of primes in over five
# thousand different ways?

from common import primes, is_prime
import functools

# Unlike problem 76, this *can* be solved by enumeration and counting. :)
# The function for generating the prime partitions is exactly analogous.

@functools.lru_cache(maxsize=None)
def ways_to_sum(n) -> set[tuple[int]]:
    """
    All the ways to sum `n`, in one or more primes.
    """
    if n <= 0: return set()
    s = set()
    if is_prime(n):
        s.add((n,))
    for p in primes(n):
        left_over = n - p
        for way in ways_to_sum(left_over):
            s.add(tuple(sorted((p,) + way)))
    return s

if __name__ == "__main__":
    n = 1
    while len(ways_to_sum(n)) < 5000:
        n += 1
    print(n)
