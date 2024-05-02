# Problem 75 (Singular Integer Right Triangles)
# =============================================
#
# It turns out that 12cm is the smallest length of wire that can be bent to
# form an integer sided right angle triangle in exactly one way, but there
# are many more examples.
#
#   12cm: (3, 4, 5)
#   24cm: (6, 8, 10)
#   30cm: (5, 12, 13)
#   36cm: (9, 12, 15)
#   40cm: (8, 15, 17)
#   48cm: (12, 16, 20)
#
# In contrast, some lengths of wire, like 20cm, cannot be bent to form an integer
# sided right angle triangle, and other lengths allow more than one solution to
# be found; for example, using 120cm it is possible to form exactly three
# different integer sided right angle triangles.
#
#   120cm: (30, 40, 50), (20, 48, 52), (24, 45, 51)
#
# Given that L is the length of the wire, for how many values of L ≤ 1_500_000
# can exactly one integer sided right angle triangle be formed?


# This seems like a straightforward search problem.
# Instead of checking all the combinations for every L,
# we can generate all small-enough Pythagorean triples, and check them.

from typing import Iterable
from collections import Counter

Triple = tuple[int, int, int]

# There is a nice way of generating all primitive Pythagorean triples:
# it uses a ternary tree, generates progressively larger triples, and
# each triple exactly once.
#
# ("Primitive" means that the 3 sides have no common multiple.)
#
# We get the non-primitive triples by scaling the primitive ones.
#
# The method is by B. Berggren (1934). For details, see:
#  https://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples

def mul_a(triple: Triple) -> Triple:
    a, b, c = triple
    return (
          a - 2*b + 2*c,
        2*a -   b + 2*c,
        2*a - 2*b + 3*c,
    )

def mul_b(triple: Triple) -> Triple:
    a, b, c = triple
    return (
          a + 2*b + 2*c,
        2*a +   b + 2*c,
        2*a + 2*b + 3*c,
    )

def mul_c(triple: Triple) -> Triple:
    a, b, c = triple
    return (
       -  a + 2*b + 2*c,
       -2*a +   b + 2*c,
       -2*a + 2*b + 3*c,
    )

def _triple_tree(triple: Triple, max_sum: int) -> Iterable[Triple]:
    for mul in (mul_a, mul_b, mul_c):
        t = mul(triple)
        if sum(t) <= max_sum:
            yield t
            yield from _triple_tree(t, max_sum)

def triple_tree(max_sum: int) -> Iterable[Triple]:
    """
    Yields all primitive Pythagorean triples,
    of length smaller than `max_sum`,
    each triple exactly once.
    """
    yield (3,4,5)
    yield from _triple_tree((3,4,5), max_sum)


if __name__ == "__main__":
    triples: Counter[int] = Counter()  # length -> number of triangles
    L = 1_500_000
    for triple in triple_tree(L):
        s = sum(triple)
        # mark off the primitive triple (k=1), and all its multiples.
        k = 1
        while k*s <= L:
            triples[k*s] += 1
            k += 1

    print(sum(1 for k, v in triples.items() if v == 1))
