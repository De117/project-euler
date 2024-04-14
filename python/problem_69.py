# Problem 69 (Totient Maximum)
# ============================
#
# Euler's totient function, Φ(n) [sometimes called the phi function],
# is defined as the number of positive integers not exceeding n which
# are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are
# all less than or equal to nine and relatively prime to nine, Φ(9) = 6.
#
#  n  |  Relatively Prime  |  Φ(n) | n/Φ(n)
# ----+--------------------+-------+--------
#  2  |    1               |   1   |  2
#  3  |    1,2             |   2   |  1.5
#  4  |    1,3             |   2   |  2
#  5  |    1,2,3,4         |   4   |  1.25
#  6  |    1,5             |   2   |  3
#  7  |    1,2,3,4,5,6     |   6   |  1.1666...
#  8  |    1,3,5,7         |   4   |  2
#  9  |    1,2,4,5,7,8     |   6   |  1.5
#  10 |    1,3,7,9         |   4   |  2.5
#
# It can be seen that n=6 produces a maximum n/Φ(n) for n ≤ 10.
#
# Find the value of n ≤ 1_000_000 for which n/Φ(n) is a maximum.
from common import euler_phi

if __name__ == "__main__":
    print(max(range(1, 1_000_000+1), key=lambda n: n/euler_phi(n)))
