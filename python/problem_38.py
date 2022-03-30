# Problem 38 (Pandigital multiples)
# =================================
#
# Take the number 192 and multiply it by each of 1, 2, and 3:
#
#     192 × 1 = 192
#     192 × 2 = 384
#     192 × 3 = 576
#
# By concatenating each product we get the 1 to 9 pandigital, 192384576.
# We will call 192384576 the concatenated product of 192 and (1,2,3)
#
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
# and 5, giving the pandigital, 918273645, which is the concatenated product
# of 9 and (1,2,3,4,5).
#
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as
# the concatenated product of an integer with (1,2, ... , n) where n > 1?


import itertools
import math


# My approach is similar to problem 32 -- there aren't that many pandigital
# numbers.


def generate_all_n_pandigital_numbers(n: int):
    assert 0 <= n <= 10
    for digits in itertools.permutations("123456789"[:n]):
        yield "".join(digits)


def multiply(number: int, n: int) -> str:
    return "".join(str(number*i) for i in range(1, n+1))

# How do we know which number, multiplied so by (1,2, ... , n), generated a
# 1 to 9 pandigital number? Since the tuple always begins with 1, the original
# number must be a prefix of the pandigital number.
if __name__ == "__main__":

    results = []

    for pan in generate_all_n_pandigital_numbers(9):

        # Since n > 1, it can take up no more than half of its length.
        for i in range(1, len(pan)//2 + 1):
            number = int(pan[:i])

            # We also know that n cannot be more than 9,
            # or less for longer numbers.
            upper_bound = math.ceil(9/i)
            for n in range(1, upper_bound+1):
                if multiply(number, n) == pan:
                    results.append(pan)
                    break

    print(max(results))
