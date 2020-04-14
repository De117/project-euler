# Problem 33 (Digit cancelling fractions)
# =======================================
#
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician
# in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which
# is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less
# than one in value, and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms,
# find the value of the denominator.

# We're looking for fractions:
#  - without both numerator & denominator ending in same number (non-trivial)
#  - less than one (numerator < denominator)
#  - two digits in numerator and denominator (max. (99-9)² possibilities)
from fractions import Fraction
from common import product


if __name__ == "__main__":
    fractions = []

    for numerator in range(10,100):
        a = numerator // 10
        b = numerator % 10

        for denominator in range(10,100):
            c = denominator // 10
            d = denominator % 10

            if numerator >= denominator:  # must be < 1
                continue

            if b == d:  # must be non-trivial
                continue

            # curiously simplified fraction
            try:
                if a == d:
                    curiously_simplified = Fraction(b, c)
                elif b == c:
                    curiously_simplified = Fraction(a, d)
                elif a == c:
                    curiously_simplified = Fraction(b, d)
                else:
                    continue  # definitely not a curious fraction
            except ZeroDivisionError:
                continue

            # properly simplified fraction
            f = Fraction(numerator, denominator)

            if f == curiously_simplified:
                fractions.append(f)

    print(product(fractions).denominator)
