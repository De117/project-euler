# Problem 70 (Totient Permutation)
#
# Euler's totient function, Φ(n) [sometimes called the phi function], is used
# to determine the number of positive numbers less than or equal to n which are
# relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less nine
# and relatively prime to nine, Φ(9) = 6.
# The number 1 is considered to be relatively prime to every positive number, so Φ(1) = 1.
#
# Interestingly, Φ(87109) = 79180, and it can be seen that 87109 is a permutation of 79180.
#
# Find the value of n, 1 < n < 10^7, for which Φ(n) is a permutation of n and the ratio
# n/Φ(n) produces a minimum.
from common import euler_phi

def are_permutations(n1: int, n2: int) -> bool:
    return sorted(str(n1)) == sorted(str(n2))

candidates = []
for n in range(2, 10_000_000):
    phi_n = euler_phi(n)
    if are_permutations(n, phi_n):
        candidates.append((n, phi_n))

print(min(candidates, key=lambda t: t[0]/t[1])[0])
