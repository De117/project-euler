# Sub-string divisibility
# Problem 43
#
# The number, 1406357289, is a 0 to 9 pandigital number because it is
# made up of each of the digits 0 to 9 in some order, but it also has
# a rather interesting sub-string divisibility property.
#
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on.
# In this way, we note the following:
#
#     d2d3d4=406 is divisible by 2
#     d3d4d5=063 is divisible by 3
#     d4d5d6=635 is divisible by 5
#     d5d6d7=357 is divisible by 7
#     d6d7d8=572 is divisible by 11
#     d7d8d9=728 is divisible by 13
#     d8d9d10=289 is divisible by 17
#
# Find the sum of all 0 to 9 pandigital numbers with this property.

import itertools

def generate_all_pandigital_numbers():
    """Generate all pandigital numbers (as strings)."""
    for digits in itertools.permutations("0123456789"):
        if digits[0] != "0":
            yield "".join(digits)


def in_triples(l: list):
    """Returns triples in l, offset by one."""
    return zip(l, l[1:], l[2:])


def p(n: str):
    """Check if property holds for n (as string)."""

    # Setting primes[0] to 1 means we can skip the special case of d₁d₂d₃
    primes = [1,2,3,5,7,11,13,17,19,23]

    for i, (d1, d2, d3) in enumerate(in_triples(n)):
        substring = d1 + d2 + d3
        if int(substring) % primes[i] != 0:
            return False

    return True


if __name__ == "__main__":
    total = 0
    have_property = []
    for n in generate_all_pandigital_numbers():
        if p(n):
            have_property.append(int(n))
    print(f"{len(have_property)} numbers have the property: {have_property}")
    print(f"Their sum is {sum(have_property)}")
