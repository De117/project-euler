# Problem 26 (Reciprocal cycles)
# ==============================
#
# A unit fraction contains 1 in the numerator. The decimal representation
# of the unit fractions with denominators 2 to 10 are given:
#
#     1/2	= 	0.5
#     1/3	= 	0.(3)
#     1/4	= 	0.25
#     1/5	= 	0.2
#     1/6	= 	0.1(6)
#     1/7	= 	0.(142857)
#     1/8	= 	0.125
#     1/9	= 	0.(1)
#     1/10	= 	0.1
#
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
# It can be seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring
# cycle in its decimal fraction part.

def divide_1_with(n):
    """
    Calculates 1/n.

    Returns: (cycle_length: int, decimals: [int])

        where decimals include the leading zero.
    """
    decimals = [0]
    remainders = [1]
    remainder = 10

    while remainder:

        decimal = remainder // n
        remainder = remainder % n

        if remainder in remainders:
            # We've found a cycle!
            # Of what length?
            cycle_length = len(remainders) - remainders.index(remainder)

            if decimal == decimals[-cycle_length]:
                # We don't want to duplicate the first element of the cycle
                return cycle_length, decimals
            else:
                return cycle_length, decimals + [decimal]

        decimals.append(decimal)
        remainders.append(remainder)
        remainder *= 10

    return 0, decimals


if __name__ == "__main__":
    longest_cycle_length = 0
    best_i = 0

    for i in range(2, 1000):
        cycle_length, _ = divide_1_with(i)
        if cycle_length > longest_cycle_length:
            longest_cycle_length = cycle_length
            best_i = i

    print(best_i)
