# Problem 71 (Ordered Fractions)
# ==============================
#
# Consider the fraction, n/d, where n and d are positive integers.
# If n < d and HCF(n,d) = 1, it is called a reduced proper fraction.
#
# If we list the set of reduced proper fractions for d ≤ 8 in ascending
# order of size, we get:
#
#     1    1    1    1    1    2    1    3    2   *3*   1    4    3    5    2    5    3    4    5    6    7
#    ---, ---, ---, ---, ---, ---, ---, ---, ---, ---, ---, ---, ---, ---, ---, ---, ---, ---, ---, ---, ---
#     8    7    6    5    4    7    3    8    5   *7*   2    7    5    8    3    7    4    5    6    7    8
#
# It can be seen that 2/5 is the fraction immediately to the left of 3/7.
#
# By listing the set of reduced proper fractions for d ≤ 1_000_000 in ascending
# order of size, find the numerator of the fraction immediately to the left of 3/7.
#
# Note: HCF stands for "highest common factor", a.k.a. greatest common divisor.


# From more general to more specific, we have:
#
#  1. Stern-Brocot tree. This is a binary tree of all positive rational numbers.
#     (An in-order traversal yields reduced fractions.)
#
#     Starting with (0/1, 1/1, 1/0), we generate a left and a right child from its pairs.
#     Given a pair (a/b, c/d), the child is the *mediant*, i.e. (a+c/b+d).
#
#  2. Farey tree. This is the left subtree of the Stern-Brocot tree: the one which starts
#     with (0/1, 1/2, 1/1), and yields all rational numbers between 0 and 1.
#
#  3. Farey sequence (of order n). This is an in-order traversal of a Farey tree,
#     but yielding only numbers whose denominators are ≤n.
#
# The problem describes a Farey sequence of order 1_000_000.
#
# Like with a Farey tree, an element of the Farey sequence
# is always a mediant of its neighbours.
#
# For the solution, we search the Farey tree, specifically the subtree between
# 2/5 and 3/7, and go down the rightmost path (=closest to 3/7), as deep as we
# can before the denominator exceeds 1_000_000.

Pair = tuple[int, int]

def mediant(ab: Pair, cd: Pair) -> Pair:
    a, b = ab
    c, d = cd
    return (a+c, b+d)

left = (2, 5)
right = (3, 7)
while True:
    num, denom = mediant(left, right)
    if denom > 1_000_000:
        break
    left = (num, denom)
print(left[0])
