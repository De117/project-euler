# Problem 27 (Quadratic primes)
# =============================
# 
# Euler discovered the remarkable quadratic formula:
# 
#     n² + n + 41
# 
# It turns out that the formula will produce 40 primes for the consecutive
# integer values 0≤n≤39. However, when n=40, 40²+40+41=40(40+1)+41 is divisible
# by 41, and certainly when n=41, 41²+41+41 is clearly divisible by 41.
# 
# The incredible formula n²−79n+1601 was discovered, which produces 80 primes
# for the consecutive values 0≤n≤79. The product of the coefficients, −79 and
# 1601, is −126479.
# 
# Considering quadratics of the form:
# 
#     n²+an+b , where |a|<1000 and |b|≤1000
# 
#   where |n| is the modulus/absolute value of n
#   e.g. |11|=11 and |−4|=4
# 
# Find the product of the coefficients, a and b, for the quadratic expression
# that produces the maximum number of primes for consecutive values of n,
# starting with n=0.
from common import is_prime


if __name__ == "__main__":

    longest_prime_sequence = []
    a_best, b_best = None, None

    for a in range(-999, 1000):
        for b in range(-1000, 1000+1):

            prime_sequence = []

            n = 0
            val = n**2 + a*n + b
            while is_prime(val):
                prime_sequence.append(val)
                n += 1
                val = n**2 + a*n + b

            if len(prime_sequence) > len(longest_prime_sequence):
                longest_prime_sequence = prime_sequence
                a_best, b_best = a, b

    # print(f"Longest prime sequence is {len(longest_prime_sequence)} long:")
    # print(longest_prime_sequence)
    # print(f"a*b = {a_best}*{b_best} = {a_best*b_best}")
    print(a_best * b_best)
