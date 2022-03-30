# Problem 35 (Circular primes)
#
# The number, 197, is called a circular prime because all rotations
# of the digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100:
# 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?
from common import primes, is_prime

if __name__ == "__main__":
    circular_primes = []
    for p in primes():
        if p > 1000000:
            break

        # check rotations
        s = str(p)
        for i in range(len(s)):
            s = s[1:] + s[:1]
            if not is_prime(int(s)):
                break
        else:
            circular_primes.append(p)

    print(len(circular_primes))
