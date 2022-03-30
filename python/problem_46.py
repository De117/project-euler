# Problem 46 (Goldbach's other conjecture)
# ========================================
#
# It was proposed by Christian Goldbach that every odd composite
# number can be written as the sum of a prime and twice a square.
#
#   9 = 7 + 2×1²
#   15 = 7 + 2×2²
#   21 = 3 + 2×3²
#   25 = 7 + 2×3²
#   27 = 19 + 2×2²
#   33 = 31 + 2×1²
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as
# the sum of a prime and twice a square?
import math
from common import primes


# Most odd composites *can* be written as the sum of a prime and twice a square.
# So, instead of going through odd numbers and checking if can they be written
# like that, it should be faster to just sieve them out.

if __name__ == "__main__":

    upper_bound = 10**2
    while True:
        upper_bound *= 10

        # Sieve, with even numbers marked off
        r = {i: (i % 2 == 0) for i in range(2, upper_bound)}

        squares_to_consider = [i**2 for i in range(1, math.ceil((upper_bound / 2)**0.5))]

        # Mark off primes and "prime + 2*square" numbers
        for p in primes(upper_bound):
            r[p] = True

            for square in squares_to_consider:
                r[p + 2*square] = True

        found = [k for k in r if not r[k]]
        if found:
            print(found[0])
            break
