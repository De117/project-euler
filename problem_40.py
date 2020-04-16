# Problem 40 (Champernowne's constant)
# ====================================
#
# An irrational decimal fraction is created by concatenating the positive integers:
#
#   0.123456789101112131415161718192021...
#                ^
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If d_n represents the nth digit of the fractional part, find the value
# of the following expression:
#
#     d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000
#
def the_fraction():
    i = 1
    while True:
        yield from str(i)
        i += 1

if __name__ == "__main__":

    result = 1

    for i, d_n in enumerate(the_fraction()):

        if i + 1 in (1, 10, 100, 1000, 10000, 100000, 1000000):
            result *= int(d_n)
            if i + 1 == 10**6:
                break

    print(result)
