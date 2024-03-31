# Problem 64 (Odd Period Square Roots)
# ====================================
#
# All square roots are periodic when written as continued fractions and can be written in the form:
#
#                           1
#        √(N) = a_0 + -----------------
#                                1
#                      a_1  + ---------
#                             a_2 + ...
#
#
# For example, let us consider √23:
#
#     √23 = 4 + √23 - 4 = 4 + ...
#
# If we continue we would get the following expansion:
#
#                           1
#        √23   = 4  + -----------------
#                                1
#                       1   + ---------
#                              3  + ...
#
# The process can be summarised as follows:
#
#     a0 = 4, 1/(√23-4) =  (√23+4)/7  = 1 + (√23-3)/7
#     a1 = 1, 7/(√23-3) = 7(√23+3)/14 = 3 + (√23-3)/2
#     a2 = 3, 2/(√23-3) = 2(√23+3)/14 = 1 + (√23-4)/7
#     a3 = 1, 7/(√23-4) = 7(√23+4)/7  = 8 + √23 - 4
#     a4 = 8, 1/(√23-4) =  (√23+4)/7  = 1 + (√23-3)/7
#     a5 = 1, 7/(√23-3) = 7(√23+3)/14 = 3 + (√23-3)/2
#     a6 = 3, 2/(√23-3) = 2(√23+3)/14 = 1 + (√23-4)/7
#     a7 = 1, 7/(√23-4) = 7(√23+4)/7  = 8 + √23 - 4
#
# It can be seen that the sequence is repeating.
# For conciseness, we use the notation √23 = [4; (1,3,1,8)],
# to indicate that the block (1,3,1,8) repeats indefinitely.
#
# The first ten continued fraction representations of (irrational) square roots are:
#
# √2 = [1;(2)], period=1
# √3 = [1;(1,2)], period=2
# √5 = [2;(4)], period=1
# √6 = [2;(2,4)], period=2
# √7 = [2;(1,1,1,4)], period=4
# √8 = [2;(1,4)], period=2
# √10 = [3;(6)], period=1
# √11 = [3;(3,6)], period=2
# √12 = [3;(2,6)], period=2
# √13 = [3;(1,1,1,1,6)], period=5
#
# Exactly four continued fractions, for N ≤ 13, have an odd period.
#
# How many continued fractions for N ≤ 10_000 have an odd period?


# It turns out there is a nice formula for this.
# See: https://en.wikipedia.org/wiki/Periodic_continued_fraction#Length_of_the_repeating_block

from math import floor, sqrt

def root_as_continued_fraction(n: int) -> tuple[int, list[int]]:
    """
    Given a non-square natural number, returns its root
    as a continued fraction, in the format (a0, cycle).

    Raises ValueError if `n` is a square.
    """
    try:
        m = 0
        d = 1
        a = floor(sqrt(n))
        a0 = a
        repeating_part = []
        while True:
            m = d * a - m
            d = (n - m**2) // d
            a = floor((a0 + m)//d)
            if (m,d,a) in repeating_part:
                break
            repeating_part.append((m,d,a))

        return a0, [a for (_,_,a) in repeating_part]

    except ZeroDivisionError:
        raise ValueError(f"{n} has a rational root!")


number_of_cycles_with_odd_period = 0
for n in range(10_000+1):
    try:
        a0, cycle = root_as_continued_fraction(n)
        if len(cycle) % 2 != 0:
            number_of_cycles_with_odd_period += 1
    except ValueError:
        pass
print(number_of_cycles_with_odd_period)
