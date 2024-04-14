# Problem 68 (Magic 5-gon Ring)
# =============================
#
# Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6,
# and each line adding to nine.
#
#
#        4
#         \
#          3
#         / \
#        1 - 2 - 6
#       /
#      5
#
# Working clockwise, and starting from the group of three with the numerically lowest
# external node (4,3,2 in this example), each solution can be described uniquely.
# For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.
#
# It is possible to complete the ring with four different totals: 9, 10, 11, and 12.
# There are eight solutions in total.
#
#  Total         Solution Set
#    9       4,2,3; 5,3,1; 6,1,2
#    9       4,3,2; 6,2,1; 5,1,3
#   10       2,3,5; 4,5,1; 6,1,3
#   10       2,5,3; 6,3,1; 4,1,5
#   11       1,4,6; 3,6,2; 5,2,4
#   11       1,6,4; 5,4,2; 3,2,6
#   12       1,5,6; 2,6,4; 3,4,5
#   12       1,6,5; 3,5,4; 2,4,6
#
# By concatenating each group it is possible to form 9-digit strings;
# the maximum string for a 3-gon ring is 432621513.
#
# Using the numbers 1 to 10, and depending on arrangements, it is possible
# to form 16- and 17-digit strings. What is the maximum 16-digit string for
# a "magic" 5-gon ring?
#
#                      O
#                       \
#                         \
#                          O
#                        /   \       O
#                      /       \    /
#                    /           \ /
#                   O             O
#                  /\            /
#                 /  \          /
#                O    \        /
#                      O------O----O
#                       \
#                        \
#                         O

import itertools, operator
from typing import Iterable

# We represent an n-gon as a list of "spike-vertex-nextvertex" lines.
# While it has redundancy, its pattern is clear, and the format easy to work with.
NGon = list[tuple[int, int, int]]

all_ngons: Iterable[NGon] = (
    [(n1, n2, n4), (n3, n4, n6), (n5, n6, n8), (n7, n8, n10), (n9, n10, n2)]
    for n1, n2, n3, n4, n5, n6, n7, n8, n9, n10 in itertools.permutations(range(1, 10+1))
)

def canonicalize(lines: NGon) -> NGon:
    # The lines should start from the smallest tip.
    index_of_smallest_tip = argmin(lines, key=lambda tup: tup[0])
    return rotl(index_of_smallest_tip, lines)

def rotl(n: int, xs):
    assert -len(xs) <= n <= len(xs)
    return list(itertools.chain(xs[n:], xs[:n]))

def argmin(iterable, key=lambda x: x):
    return min(enumerate(iterable), key=lambda t: key(t[1]))[0]


def is_magic(ngon: NGon) -> bool:
    s = sum(ngon[0])
    for line in ngon[1:]:
        if sum(line) != s:
            return False
    return True

if __name__ == "__main__":
    magic_ngons = [ngon for ngon in all_ngons if is_magic(ngon)]

    strings = {
        "".join(str(int(n)) for n in itertools.chain(*lines))
        for lines in map(canonicalize, magic_ngons)
    }
    print(max(map(int, [s for s in strings if len(s) == 16])))
