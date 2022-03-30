# Problem 36 (Double-base palindromes)
# ====================================
#
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million,
# which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include
# leading zeros.)
if __name__ == "__main__":
    double_base_palindromes = []

    for i in range(1,1000000):
        s1 = str(i)
        s2 = bin(i)[2:]
        if s1 == s1[::-1] and s2 == s2[::-1]:
            double_base_palindromes.append(i)

    print(sum(double_base_palindromes))
