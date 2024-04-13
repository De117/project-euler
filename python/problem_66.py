# Problem 66 (Diophantine equation)
# =================================
#
# Consider quadratic Diophantine equations of the form:
#
#     x² - Dy² = 1
#
# For example, when D = 13, the minimal solution in x is 649² - 13*180² = 1.
#
# It can be assumed that there are no solutions in positive integers when D is square.
#
# By finding minimal solutions in x for D = {2,3,5,6,7}, we obtain the following:
#
#     3² - 2*2² = 1
#     2² - 3*1² = 1
#     9² - 5*4² = 1
#     5² - 6*2² = 1
#     8² - 7*3² = 1
#
# Hence, by considering minimal solutions in x for D ≤ 7, the largest is obtained when D = 5.
#
# Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.



# This particular equation is known as Pell's equation.
# If D is non-square, it has infinitely many integral solutions: convergents of √D.
# ("Convergents" meaning sums of continued fractions; for example, see problem 65.)
#
# Using the same notation as in problem 65, we can write
#
#   √D = [a0; c_1, c_2, ..., c_p]
#
# and for indexing, say that a0 is the 0th convergent.
# Then the desired minimal-x solution will be the
#
#    (p-1)th convergent, for even p,
#    (2p-1)th convergent, for odd p.
from problem_64 import root_as_continued_fraction
from problem_65 import sum_continued_fraction

from itertools import islice, chain, cycle
from fractions import Fraction
from typing import Union

def is_square(n: int) -> bool:
    root = n**0.5
    return round(root)**2 == n

def yield_(x):
    yield x

def take(n, iterable):
    return list(islice(iterable, n))

def find_minimal_x(D: int) -> Union[int, None]:
    if is_square(D):
        return None

    a0, repeating_part = root_as_continued_fraction(D)
    p = len(repeating_part)

    if p % 2 == 0:
        k = p-1
    else:
        k = 2*p - 1

    terms = take(k+1, chain(yield_(a0), cycle(repeating_part)))
    return sum_continued_fraction(terms)


if __name__ == "__main__":
    solution = (0, Fraction(0, 1))
    for D in range(1001):
        if (fraction := find_minimal_x(D)) is not None:
            if fraction.numerator > solution[1].numerator:
                solution = (D, fraction)

    print(solution[0])
