# Problem 28 (Number spiral diagonals)
# ====================================
#
# Starting with the number 1 and moving to the right in a clockwise direction
# a 5 by 5 spiral is formed as follows:
#
#     21 22 23 24 25
#     20  7  8  9 10
#     19  6  1  2 11
#     18  5  4  3 12
#     17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
# formed in the same way?

# The diagonal elements are:
#  1, 3, 5, 7, 9, 13, 17, 21, 25 (, 31, 37, 43, 49, 57...)
#
# Note the distances:
#  2, 2, 2, 2, 4, 4, 4, 4, 6, 6, 6, 6, 8...
#
# It's apparent that, if the final diameter has D elements in it,
# the distance between two adjacent diagonal elements will be D - 1.
#
# For a 1001x1001 spiral, we then have:
if __name__ == "__main__":

    D = 1001

    total = i = 1
    diameters = range(3, D+1, 2)

    for d in diameters:
        for _ in range(4):
            i += (d - 1)
            total += i

    print(total)
