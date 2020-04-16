# Problem 41 (Pandigital prime)
#
# We shall say that an n-digit number is pandigital if it makes use of
# all the digits 1 to n exactly once. For example, 2143 is a 4-digit
# pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?
import itertools
from common import is_prime

def generate_all_n_pandigital_numbers(n: int):
    assert 0 <= n <= 10
    for digits in itertools.permutations("123456789"[:n]):
        yield "".join(digits)

if __name__ == "__main__":

    largest_pandigital_prime = 0

    for n in range(1,9+1):
        for pan in generate_all_n_pandigital_numbers(n):
            pan = int(pan)
            if is_prime(pan) and pan > largest_pandigital_prime:
                largest_pandigital_prime = pan

    print(largest_pandigital_prime)
