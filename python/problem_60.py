# Problem 60 (Prime pair sets)
# ============================
#
# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two
# primes and concatenating them in any order the result will always be prime.
# For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of
# these four primes, 792, represents the lowest sum for a set of four
# primes with this property.
#
# Find the lowest sum for a set of five primes for which
# any two primes concatenate to produce another prime.

from common import is_prime, primes
import itertools

def prop(s: set[int]) -> bool:
    """The property."""
    return all(
        is_prime(int(str(a)+str(b)))
        for (a,b) in itertools.product(s, s)
        if a != b
    )

# The solution set has another nice property:
# the "remarkable" property holds for all its subsets, too.
#
# So we can build the solution set up as a union of its subsets.
# As a base, we have size-1 sets, each containing 1 prime number;
# the property obviously holds for them.
#
# Now, what we'd want here is a best-first search:
#
#   select a "length" of size-1 sets (2, 3, 5, ... N},
#   build up all size-2 sets that you can,
#   then size-3 sets,
#   then size-4 sets,
#   then size-5 sets.
#
# If our "length" includes all primes in the solution, we will have found it.
# Otherwise, we won't find any size-5 sets (and maybe no smaller ones, either),
# so we extend the length and try again.

# But for now, a single arbitrary "length" will do.
sets_of_size = {}
sets_of_size[1] = {frozenset({p}) for p in primes(1100)}
print(f"Sets of size {1}: {len(sets_of_size[1])}, min {set(min(sets_of_size[1], key=sum))}, max {set(max(sets_of_size[1], key=sum))}")

for n in (2,3,4,5):
    sets_of_size[n] = set()
    for i, s1 in enumerate(sets_of_size[1]):
        for s2 in sets_of_size[n-1]:
            s = s1 | s2
            if len(s) == n and prop(s):
                sets_of_size[n].add(s)
    if not sets_of_size[n]:
        print(f"No set of size {n}!")
        break
    print(f"Sets of size {n}: {len(sets_of_size[n])}, min {set(min(sets_of_size[n], key=sum))}, max {set(max(sets_of_size[n], key=sum))}")

try:
    print("Solution:", sum(min(sets_of_size[5], key=sum)))
except KeyError:
    pass
