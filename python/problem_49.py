# Problem 49 (Prime permutations)
# ===============================
#
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
# increases by 3330, is unusual in two ways: (i) each of the three terms
# are prime, and, (ii) each of the 4-digit numbers are permutations of one
# another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
# exhibiting this property, but there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this sequence?
from common import primes, is_prime
from collections import Counter
import itertools


def are_permutations(n1, n2):
    return Counter(str(n1)) == Counter(str(n2))


if __name__ == "__main__":

    four_digit_primes = itertools.takewhile(lambda n: n < 10000, primes())
    four_digit_primes = [p for p in four_digit_primes if p >= 1000]

    for i, p1 in enumerate(four_digit_primes[:-2]):

        for p2 in four_digit_primes[i+1:]:
            step = p2 - p1
            p3 = p2 + step

            if are_permutations(p1, p2) and are_permutations(p2, p3):
                if is_prime(p2) and is_prime(p3):
                    if p1 != 1487:
                        print(f"{p1}{p2}{p3}")
