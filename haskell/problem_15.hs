-- Problem 15 (Lattice paths)
-- ==========================
--
-- Starting in the top left corner of a 2×2 grid, and only being able to move
-- to the right and down, there are exactly 6 routes to the bottom right corner.
--
--    ooooooo    oooo--+    oooo--+
--    |  |  o    |  o  |    |  o  |
--    +--+--o    +--oooo    +--o--+
--    |  |  o    |  |  o    |  o  |
--    +--+--V    +--+--V    +--ooo>
--
--    o--+--+    o--+--+    o--+--+
--    o  |  |    o  |  |    o  |  |
--    ooooooo    oooo--+    o--+--+
--    |  |  o    |  o  |    o  |  |
--    +--+--V    +--ooo>    oooooo>
--
-- How many such routes are there through a 20×20 grid?

-- We have 20 "down" moves and 20 "right" moves to choose from.
-- The number of different arrangements is the number of multiset
-- permutations of the set of 40 moves of 2 types: 40!/(20!*20!).

fact n = product [1..n]

main = print (fact 40 `div` ((fact 20) * (fact 20)))
