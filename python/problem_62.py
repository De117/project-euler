# Problem 62 (Cubic Permutations)
# ===============================
#
# The cube, 41063625 (345^3), can be permuted to produce two other cubes:
# 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest
# cube which has exactly three permutations of its digits which are also cube.
#
# Find the smallest cube for which exactly five permutations of its digits are cube.
import math, itertools, functools

def is_cube(n: int) -> bool:
    root = n**(1/3)
    rounded = round(root)
    # The second part of the check avoids cases like like
    #  8012006010**(1/3) == 2001.0000007492497  # not 2001**3
    #  8012006001**(1/3) == 2000.999999999999   # is 2001**3
    return math.isclose(root, rounded) and rounded**3 == n


# The naive way is to go over all cubes and check each cube's permutations.
def naive_way() -> int:
    i = 0
    while True:
        i += 1
        cube = i**3
        cubic_permutations = set()
        for permuted_digits in itertools.permutations(str(cube)):
            if permuted_digits[0] == "0":
                continue  # we don't consider permutations which drop digits

            n = int("".join(permuted_digits))
            if is_cube(n):
                cubic_permutations.add(n)

        if len(cubic_permutations) == 5:
            return min(cubic_permutations)

# The problem with this one is that, to find the solution N, we'll check
#
#    ∑       ⌈log_10(k**3)⌉!
#  k = 1..N
#
#  permutations. Factorials grow very quickly!
#
# It also isn't efficient, because
#  1. we generate permutations which are not valid numbers,
#  2. we check permutations which aren't cubes, and
#  2. even cubic permutations are checked more than once.

# But all permutations of a string form an equivalence class:
# two strings are permutations iff the multisets of their characters are equal.
#
# With a look-up table, we can go over only cubes, exactly once per cube.

def digits(n: int) -> str:
    """
    A "hashable multiset" of a number's digits.

    (collections.Counter would be better, if it were hashable.)
    """
    return "".join(sorted(str(n)))


equivalence_classes = {}


# Note that the problem says *exactly 5* permutations.
# If we have an equivalence class of size 5 _now_, how do we know
# that there are no unseen permutations waiting?
#
# Length. All members of our equivalence class will have the same length.
#         If we've seen all the cubes of that length, there can be no more.

i = 0
last_length = 0
while True:
    i += 1
    cube = i**3
    ds = digits(cube)
    try:
        equivalence_classes[ds].add((i, cube))
    except KeyError:
        equivalence_classes[ds] = {(i, cube)}

    current_length = len(ds)
    if current_length > last_length:
        classes_of_length_5 = [ec for ec in equivalence_classes.values() if len(ec) == 5]
        cubes = functools.reduce(set.union, classes_of_length_5, set())
        if cubes:
            print(min(cubes))
            break

        last_length = current_length
