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

# The naive approach works well enough:
def chain_length(n: int) -> int:
    length = 0
    current = n
    seen = set()
    while current not in seen:
        seen.add(current)
        length += 1
        current = sum(fact(d) for d in digits(current))
    return length

if __name__ == "naive":
    total = 0
    for n in range(1, 1_000_000):
        if chain_length(n) == 60:
            total += 1
    print(total)

# But we can do better with some caching.
# A "chain" is really a prefix + a cycle.
#
# They have a few nice properties:
#   * a number is either on a prefix or on a cycle
#   * cycles cannot overlap
#   * there are only a few cycles altogether

if __name__ == "__main__":
    path_lengths: dict[int, int] = {}  # number -> path (prefix + cycle) length

    N = 1_000_000
    for n in range(1, N):
        current = n
        seen = []  # list is just as fast as set + list
        while not (current in path_lengths.keys() or current in seen):
            seen.append(current)
            current = sum(fact(d) for d in digits(current))

        if current in path_lengths.keys():
            # We hit either:
            #  1. a number on a cycle (and it's not present in `seen`), or
            #  2. a number on the prefix of a known path.
            #
            # In either case, we know that path's length, and we can
            # calculate it for the numbers in *our* part of the prefix.
            our_part_of_prefix = seen
            for i, number in enumerate(reversed(our_part_of_prefix)):
                offset = i + 1
                path_lengths[number] = path_lengths[current] + offset

        else:
            # It's the first time that we see this path.
            cycle_start = seen.index(current)
            prefix = seen[:cycle_start]
            cycle = seen[cycle_start:]

            for number in cycle:
                path_lengths[number] = len(cycle)

            for i, number in enumerate(reversed(prefix)):
                offset = i + 1
                path_lengths[number] = len(cycle) + offset

    print(sum(1 for n in range(1, N) if path_lengths[n] == 60))
