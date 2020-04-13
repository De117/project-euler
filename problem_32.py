# Problem 32 (Pandigital products)
# ================================
#
# We shall say that an n-digit number is pandigital if it makes use of all
# the digits 1 to n exactly once; for example, the 5-digit number, 15234,
# is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
# multiplicand, multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity
# can be written as a 1 through 9 pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only
# include it once in your sum.
import itertools


# Since the number of pandigital numbers is finite and reasonably small,
# (in the millions), we can just go through all of them, and check which
# one can be split into such a product.
#
# Also, this definition of "pandigital" is slightly different than the
# one in problem 47, so I'll call it "n-pandigital".
#
def generate_all_n_pandigital_numbers(n: int):
    assert 0 <= n <= 10
    for digits in itertools.permutations("123456789"[:n]):
        yield "".join(digits)


if __name__ == "__main__":

    # We look for triples (a,b,p) such that a × b = p.
    pandigital_triples = set()

    for n in [9]:
        to_check = generate_all_n_pandigital_numbers(n)

        # Can we split any one of these into such a triple?
        #
        # A product of a k-digit and an l-digit number will have
        # r=(k+l) or r=(k+l-1) digits. So, any split must be of form k : l : r.
        #
        # Let's generate all such splits.
        splits = []
        for k,l in itertools.product(range(1,(n-2)+1), range(1,(n-2)+1)):
            r = n - k - l
            if r in (k+l, k+l-1):
                splits.append((k, l))

        # And the actual check
        for s in to_check:
            for k, l in splits:
                a = int(s[:k])
                b = int(s[k:k+l])
                p = int(s[k+l:])
                if a*b == p:
                    pandigital_triples.add((a,b,p))

    pandigital_products = set(p for (a,b,p) in pandigital_triples)
    print(sum(pandigital_products))
