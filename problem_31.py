# Problem 31 (Coin sums)
# ======================
#
# In the United Kingdom the currency is made up of pound (£) and pence (p).
# There are eight coins in general circulation:
#
#    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
#
# It is possible to make £2 in the following way:
#
#    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#
# How many different ways can £2 be made using any number of coins?

# This is a classic dynamic programming problem.
# One recursive solution would be:
options = [1,2,5,10,20,50,100,200]

def recursive(target_amount):
    """Generate all permutations that add up to the target amount."""
    for coin in options:
        if coin > target_amount:
            continue
        elif coin == target_amount:
            yield (coin,)
        else: # coin < target_amount
            for rest in recursive(target_amount - coin):
                yield (coin,) + rest

# But this can be done in another way.
def dynamic(target_amount):
    """Calculate number of all permutations that add up to the target amount."""
    cache = {0: 1}

    for amount in range(1, target_amount+1):
        # Number of all known paths that lead to this point
        ways = sum(cache[amount - coin] for coin in options if (amount - coin) in cache)
        cache[amount] = ways

    return cache[target_amount]


# However, we need combinations, not permutations.
# I see no way to calculate the number of combinations
# without somehow going through all of them.
#
# For illustration, suppose we have only 2p and 3p coins.
# The combinations for amount N are:
#
#     combinations(N-2) ⋃ combinations(N-3)
#
# ...after extending each one with the proper coin, of course.
#
# The pseudocode for the general case is:
#
#   combinations[0] = [Ø]
#   for amount in [1,2,..200]:
#       combinations[N] = union(extend(combinations[N-coin], coin) for coin in coins)
#
def dynamic_combinations(target_amount):
    combinations_for = {0: [{}]}

    for amount in range(1, target_amount+1):
        union = set()
        for coin in options:
            if amount - coin >= 0:
                for c in combinations_for[amount - coin]:
                    # extend the combination
                    c = c.copy()
                    c[coin] = c.get(coin, 0) + 1
                    # convert into canonical representation ("tuplify" it)
                    # so it's hashable
                    c = tuple(sorted(c.items()))
                    # add to union
                    union.add(c)
        
        # "untuplify" to get back dicts
        combinations_for[amount] = [dict(tup) for tup in union]

    return len(combinations_for[target_amount])


if __name__ == "__main__":
    print(dynamic_combinations(200))
