# Problem 21 (Amicable numbers)
# =============================
#
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n
# which divide evenly into n). If d(a) = b and d(b) = a, where a ≠ b, then a
# and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
# 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4,
# 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.
from common import PrimeDecomposition

def is_amicable(n):
    b = sum(PrimeDecomposition(n).get_proper_divisors())
    if b == n:
        return False
    return n == sum(PrimeDecomposition(b).get_proper_divisors())

if __name__ == "__main__":
    print(sum(i for i in range(2, 10000) if is_amicable(i)))
