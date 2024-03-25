# Problem 62 (Cubic Permutations)
# ===============================
#
# The cube, 41063625 (345^3), can be permuted to produce two other cubes:
# 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest
# cube which has exactly three permutations of its digits which are also cube.
#
# Find the smallest cube for which exactly five permutations of its digits are cube.
import math, itertools

def is_cube(n: int) -> bool:
    root = n**(1/3)
    rounded = round(root)
    # The second part of the check avoids cases like like
    #  8012006010**(1/3) == 2001.0000007492497  # not 2001**3
    #  8012006001**(1/3) == 2000.999999999999   # is 2001**3
    return math.isclose(root, rounded) and rounded**3 == n

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

    #if len(cubic_permutations) > 1:
    #    print(i, cubic_permutations)

    if len(cubic_permutations) == 5:
        print(min(cubic_permutations))
        break
