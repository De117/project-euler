# Problem 72 (Counting Fractions)
# ===============================
#
# Consider the fraction, n/d, where n and d are positive integers.
# If n < d and HCF(n,d) = 1, it is called a reduced proper fraction.
#
# If we list the set of reduced proper fractions for d ≤ 8 in ascending
# order of size, we get:
#
#     1    1    1    1    1    2    1    3    2    3    1    4    3    5    2    5    3    4    5    6    7
#    ---, ---, ---, ---, ---, ---, ---, ---, ---, ---, ---, ---, ---, ---, ---, ---, ---, ---, ---, ---, ---
#     8    7    6    5    4    7    3    8    5    7    2    7    5    8    3    7    4    5    6    7    8
#
# It can be seen that there are 21 elements in this set.
#
# How many elements would be contained in the set of reduced proper fractions for d ≤ 1_000_000?
from common import euler_phi

# For a fraction n/d, when will it have d as denominator after reduction?
# When n is coprime to d. The number of such n's is given by Euler's totient function.
print(sum(euler_phi(d) for d in range(2, 1_000_000+1)))
