# Problem 73 (Counting Fractions in a Range)
# ==========================================
#
# Consider the fraction, n/d, where n and d are positive integers.
# If n < d and HCF(n,d) = 1, it is called a reduced proper fraction.
#
# If we list the set of reduced proper fractions for d ≤ 8 in ascending
# order of size, we get:
#
#     1    1    1    1    1    2    1   *3*  *2*  *3*   1    4    3    5    2    5    3    4    5    6    7
#    ---, ---, ---, ---, ---, ---, ---, ---, ---, ---, ---, ---, ---, ---, ---, ---, ---, ---, ---, ---, ---
#     8    7    6    5    4    7    3   *8*  *5*  *7*   2    7    5    8    3    7    4    5    6    7    8
#
# It can be seen that there are 3 fractions between 1/3 and 1/2.
#
# How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12_000?

from common import PrimeDecomposition
from fractions import Fraction

one_third = Fraction(1, 3)
one_half = Fraction(1, 2)
fractions = set()
for d in range(1, 12_000+1):
    for n in range(1, d):
        fraction = Fraction(n, d)
        if one_third < fraction < one_half:
            fractions.add(fraction)
print(len(fractions))
