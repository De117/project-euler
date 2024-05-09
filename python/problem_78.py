# Problem 78 (Coin Partitions)
# ============================
#
# Let n represent the number of different ways in which coins can be separated into piles.
# For example, five coins can be separated into piles in exactly seven different ways, so
# p(5) = 7.
#
# OOOOO
# OOOO   O
# OOO   OO
# OOO   O   O
# OO   OO   O
# OO   O   O   O
# O   O   O   O   O
#
# Find the least value of n for which p(n) is divisible by one million.


# p(n) is the partition function, which can be calculated recursively.
# For details, see:
#  * https://en.wikipedia.org/wiki/Pentagonal_number_theorem
#  * https://en.wikipedia.org/wiki/Partition_function_(number_theory)

import functools

def pentagonal(n: int) -> int:
    return n * (3*n - 1) // 2


@functools.lru_cache(maxsize=None)
def num_integer_partitions(n: int) -> int:
    if n < 0: return 0
    if n == 0: return 1

    total = 0
    k = 1
    # Offsets are _generalized_ pentagonal numbers:
    # they use the same formula, but the arguments go like 0, 1, -1, 2, -2, etc.
    while n - pentagonal(k) >= 0:
        sign = 1 if k % 2 != 0 else -1
        total += sign * num_integer_partitions(n - pentagonal(k))
        total += sign * num_integer_partitions(n - pentagonal(-k))
        k += 1
    return total


if __name__ == "__main__":
    n = 0
    while True:
        n += 1
        if num_integer_partitions(n) % 1_000_000 == 0:
            print(n)
            break
