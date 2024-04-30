# Problem 74 (Digit Factorial Chains)
# -----------------------------------
#
# The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:
#
#     1! + 4! + 5! = 1 + 24 + 120 = 145
#
# Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169;
# it turns out that there are only three such loops that exist:
#
#     169 -> 363601 -> 1454 -> 169
#     871 -> 45361 -> 871
#     872 -> 45362 -> 872
#
# It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,
#
#     69 -> 363600 -> 1454 -> 169 -> 363601(-> 1454)
#     78 -> 34360 -> 871 -> 45361(-> 871)
#     540 -> 145(-> 145)
#
# Starting with 69 produces a chain of five non-repeating terms,
# but the longest non-repeating chain with a starting number below one million is sixty terms.
#
# How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

def digits(n: int) -> list[int]:
    return [int(d) for d in str(n)]

def fact(n: int) -> int:
    total = 1
    for i in range(1, n+1):
        total *= i
    return total

def chain_length(n: int) -> int:
    length = 0
    current = n
    seen = set()
    while current not in seen:
        seen.add(current)
        length += 1
        current = sum(fact(d) for d in digits(current))
    return length

if __name__ == "__main__":
    total = 0
    for n in range(1, 1_000_000):
        if chain_length(n) == 60:
            total += 1
    print(total)
