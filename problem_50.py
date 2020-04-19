# Problem 50 (Consecutive prime sum)
# ==================================
#
# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
#
# This is the longest sum of consecutive primes that adds to a prime
# below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds
# to a prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of
# the most consecutive primes?
from common import primes, is_prime
import itertools


if __name__ == "__main__":

    primes = list(itertools.takewhile(lambda p: p < 1000000, primes()))

    # Which sums add up to this prime?
    sums_adding_up_to = {p: [] for p in primes}

    for i, p in enumerate(primes):

        for run_length in range(1, len(primes) - i):
            run = primes[i : i + run_length]
            s = sum(run)

            if s > 1000000:  # We're not interested in primes above the bound
                break

            if is_prime(s):
                sums_adding_up_to[s].append(run)

    longest_sum_for = {}
    for p in primes:
        longest_sum_for[p] = max(sums_adding_up_to[p], key=len, default=[])

    p, run = max(longest_sum_for.items(), key=lambda e: len(e[1]))
    print(p)
