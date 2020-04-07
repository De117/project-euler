# Problem 10 (Summation of primes)
# ================================
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
from common import is_prime

if __name__ == "__main__":
    print(sum(i for i in range(2000000+1) if is_prime(i)))
