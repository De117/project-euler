-- Problem 24 (Lexicographic permutations)
-- =======================================
--
-- A permutation is an ordered arrangement of objects. For example, 3124 is one
-- possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
-- are listed numerically or alphabetically, we call it lexicographic order.
-- The lexicographic permutations of 0, 1 and 2 are:
--
--   012   021   102   120   201   210
--
-- What is the millionth lexicographic permutation of the digits
-- 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

-- ============================================================================
-- We can do this as:
-- ```
-- import Data.List (sort, permutations)
-- main = putStrLn $ (sort . permutations "0123456789") !! 999999
-- ```
-- but that's slower than necessary.

permutations :: (Ord a) => [a] -> [[a]]
permutations [] = []
permutations [x] = [[x]]
permutations (x:y:[]) = [[x, y], [y, x]]
permutations xs = [e:perm | (i, e) <- zip [0..] xs, perm <- permutations (deleteIndex i xs)]
    where
        deleteIndex i xs = take i xs ++ drop (i+1) xs


main = putStrLn $ (permutations "0123456789") !! 999999
