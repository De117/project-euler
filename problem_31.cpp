// Problem 31 (Coin sums)
// ======================
//
// In the United Kingdom the currency is made up of pound (£) and pence (p).
// There are eight coins in general circulation:
//
//    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
//
// It is possible to make £2 in the following way:
//
//    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
//
// How many different ways can £2 be made using any number of coins?

// This is a classic dynamic programming problem.
// If we interpret ways as "permutations", the solution is:
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <unordered_set>

#define N_COINS 8
int coins[N_COINS] = {1, 2, 5, 10, 20, 50, 100, 200};

long dynamic_permutations(int *coins, int num_coins, int target_amount) {
    long *cache = (long *)calloc(target_amount, sizeof(long));

    cache[0] = 1;

    for (int amount=1; amount <= target_amount; amount++) {
        // Number of all known paths that lead to this point
        long ways = 0;
        for (int i=0; i < num_coins; i++) {
            if (amount - coins[i] >= 0) {
                ways += cache[amount - coins[i]];
            }
        }
        cache[amount] = ways;
    }

    long result = cache[target_amount];
    free(cache);

    return result;
}


// However, we need combinations, not permutations.
// I see no way to calculate the number of combinations
// without somehow going through all of them.
//
// For illustration, suppose we have only 2p and 3p coins.
// The combinations for amount N are:
//
//     combinations(N-2) ⋃ combinations(N-3)
//
// ...after extending each one with the proper coin, of course.
//
//
// But, since this is C++, we first need to do some boilerplate ourselves.

// o===========================o
// |   HELPERS / BOILERPLATE   |
// o===========================o
class Combination {
    public:
    int counts[N_COINS];
    Combination() {
        memset(this->counts, 0, N_COINS*sizeof(int));
    };

    Combination(const Combination& other) {  // the copy constructor
        memcpy(this->counts, other.counts, N_COINS*sizeof(int));
    }

    bool operator==(const Combination& other) const {
        return 0 == memcmp(this->counts, other.counts, N_COINS*sizeof(int));
    }

    Combination& operator=(const Combination& other) {
        if (this != &other) {
            memcpy(this->counts, other.counts, N_COINS*sizeof(int));
        }
        return *this;
    }
};

namespace std {
    // Override std::hash so we don't have to provide it explicitly
    template <> struct hash<Combination> {
        size_t operator()(const Combination & c) const {
            static_assert(N_COINS == 8, "Update the hash function!");
            return (2 * c.counts[0] + 3 * c.counts[1] + 5 * c.counts[2] + 7 * c.counts[3]
                  + 11 * c.counts[4] + 13 * c.counts[5] + 17 * c.counts[6] + 19 * c.counts[7]);
        };
    };
}

// o=========================o
// |   THE ACTUAL FUNCTION   |
// o=========================o

long dynamic_combinations(int *coins, int num_coins, int target_amount)
{
    std::unordered_set<Combination> *combinations_for = new std::unordered_set<Combination>[1 + target_amount];

    // There's only one way to get 0, and that's using 0 coins.
    combinations_for[0].insert(Combination());

    // In general, the number of combinations for N is:
    //
    //    UNION       extended(combinations_for[N-c])
    //   (c ∈ coins)
    for (int amount=1; amount <= target_amount; amount++) {

        for (int i=0; i < num_coins; i++) {
            if (amount - coins[i] >= 0) {
                // Extend each combination with the extra coin
                for (Combination c : combinations_for[amount - coins[i]]) {
                    c.counts[i] += 1;
                    combinations_for[amount].insert(c);
                }
            }
        }
    }

    return combinations_for[target_amount].size();
}


int main() {
    assert(2614632708599399614 == dynamic_permutations(coins, N_COINS, 80));
    printf("%ld\n", dynamic_combinations(coins, N_COINS, 200));
    return 0;
}
