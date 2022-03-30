# Problem 37 (Truncatable primes)
# ===============================
#
# The number 3797 has an interesting property. Being prime itself, it is
# possible to continuously remove digits from left to right, and remain
# prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
# right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable
# from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
from common import primes, is_prime

if __name__ == "__main__":
    primes_truncatable_both_ways = []
    for p in primes():

        # Is it truncatable from left to right?
        s = str(p)
        if not all(is_prime(int(s[i:])) for i in range(1,len(s))):
            continue

        # Is it truncatable from right to left?
        if not all(is_prime(int(s[:i])) for i in range(1,len(s))):
            continue

        if p not in (2,3,5,7):
            primes_truncatable_both_ways.append(p)

        if len(primes_truncatable_both_ways) == 11:
            break

    print(sum(primes_truncatable_both_ways))
