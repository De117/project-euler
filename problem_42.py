# Problem 42 (Coded triangle numbers)
#
# The n-th term of the sequence of triangle numbers is given by, t_n = ½n(n+1);
# so the first ten triangle numbers are:
#
#   1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding to its
# alphabetical position and adding these values we form a word value.
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t_10.
# If the word value is a triangle number then we shall call the
# word a triangle word.
#
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text
# file containing nearly two-thousand common English words, how many are
# triangle words?
import math

def triangle_numbers(less_than=math.inf):
    n = 0
    last_number = 0
    while last_number < less_than:
        last_number = n * (n + 1) // 2
        yield last_number
        n += 1


if __name__ == "__main__":

    with open("p042_words.txt") as f:
        words = [w.strip("\"") for w in f.read().split(",")]

    numbers = [sum(ord(c) - ord("A") + 1 for c in word) for word in words]

    triangle_nums = set(triangle_numbers(less_than=max(numbers)))

    print(len([n for n in numbers if n in triangle_nums]))
