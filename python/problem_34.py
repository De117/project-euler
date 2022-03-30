# Problem 34 (Digit factorials)
#
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial
# of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.


# Again, we cannot go through *all* numbers. We need a stopping criterion.
#
# When a new digit is added, the number grows (up to) elevenfold; meanwhile,
# the sum of the digits' factorials grows by at most 9! (=362880). It follows
# that the sum must, sooner or later, permanently fall behind the numbers.
#
# The numbers overtake the sum's speed when going from 6 to 7 digits.
# They completely overtake the sum when going from 7 to 8 digits, since
# the largest possible sum there is 8*9! = 2903040, less than the smallest
# possible number.
#
# This gives us an upper bound.

from common import product

def factorial(n: int):
    return product(range(1,n+1))

if __name__ == "__main__":
    curious_numbers = []
    for i in range(3, 2903040):
        if sum(factorial(int(c)) for c in str(i)) == i:
            curious_numbers.append(i)

    print(sum(curious_numbers))
