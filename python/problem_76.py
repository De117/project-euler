# Problem 76 (Counting Summations)
# ================================
#
# It is possible to write five as a sum in exactly six different ways:
#
#     4 + 1
#     3 + 2
#     3 + 1 + 1
#     2 + 2 + 1
#     2 + 1 + 1 + 1
#     1 + 1 + 1 + 1 + 1
#
# How many different ways can one hundred be written as a sum of at least two positive integers?

# The more natural way of looking at this is: in how many ways can 100 be
# partitioned into positive integers? This is called the partition function, p(n).
#
# The solution is then p(100) - 1. (One way is to have just 100 on its own.)

# We could generate the partitions explicitly...
import functools

@functools.lru_cache
def ways_to_sum(n) -> set[tuple[int]]:
    """
    All the ways to sum `n`, in one or more positive integers.
    """
    if n <= 0: return set()
    s = set()
    s.add((n,))
    for k in range(1, n):
        left_over = n - k
        for way in ways_to_sum(left_over):
            s.add(tuple(sorted((k,) + way)))
    return s

# ...but it's much faster to just calculate p(n) directly.
from problem_78 import num_integer_partitions
if __name__ == "__main__":
    print(num_integer_partitions(100) - 1)
