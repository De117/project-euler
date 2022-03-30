# Problem 15 (Lattice paths)
# ==========================
#
# Starting in the top left corner of a 2×2 grid, and only being able to move
# to the right and down, there are exactly 6 routes to the bottom right corner.
#
#    ooooooo    oooo--+    oooo--+
#    |  |  o    |  o  |    |  o  |
#    +--+--o    +--oooo    +--o--+
#    |  |  o    |  |  o    |  o  |
#    +--+--V    +--+--V    +--ooo>
#
#    o--+--+    o--+--+    o--+--+
#    o  |  |    o  |  |    o  |  |
#    ooooooo    oooo--+    o--+--+
#    |  |  o    |  o  |    o  |  |
#    +--+--V    +--ooo>    oooooo>
#
# How many such routes are there through a 20×20 grid?


#
#  "Starting in the top left corner,
#    and moving only right or down,
#     in how many ways can we get to the bottom right corner?"
#
#
# Now, the Manhattan distance between the top left and bottom right
# corners is constant -- we'll always cross the same distance, 2 * side length.
#
# For an n×n grid, we have n "right" moves and n "down" moves.
# In how many ways can we use them up?
#
#
# That's 2n elements in total, which can be arranged in (2n)! ways.
# But we want to ignore the distinctions between "down" moves; a reduction by
# a factor of n!. Same thing with "right" moves -- another reduction by a
# factor of n!.
#
# So that's (2n)!/(n!⋅n!) ways in total.

def fact(n):
    total = 1
    for i in range(n):
        total *= n
    return total

if __name__ == "__main__":
    print(fact(40) // (fact(20) * fact(20)))
