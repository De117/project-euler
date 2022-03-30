-- Problem 14 (Longest Collatz sequence)
-- =====================================
--
-- The following iterative sequence is defined for the set of positive integers:
--
--     n → n/2 (n is even)
--     n → 3n + 1 (n is odd)
--
-- Using the rule above and starting with 13, we generate the following sequence:
--     13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
--
-- It can be seen that this sequence (starting at 13 and finishing at 1)
-- contains 10 terms. Although it has not been proved yet (Collatz Problem),
-- it is thought that all starting numbers finish at 1.
--
-- Which starting number, under one million, produces the longest chain?
--
-- NOTE: Once the chain starts the terms are allowed to go above one million.

collatzNum :: (Integral a) => a -> a
collatzNum n
    | n == 1    = 0
    | even n    = 1 + collatzNum (n `div` 2)
    | otherwise = 1 + collatzNum (3*n + 1)

-- A slower, but cleaner version:
--
-- import Data.List (maximumBy)
-- import Data.Ord (comparing)
-- solution = maximumBy (comparing collatzNum) $ [1..1000000] :: Int

solution = fst . foldl f (0, 0) $ [1..1000000] :: Int
    where
        f :: (Integral a) => (a, a) -> a -> (a, a)
        f (bestN, bestLen) n | thisLen > bestLen = (n, thisLen)
                             | otherwise         = (bestN, bestLen)
            where thisLen = collatzNum n

main = print solution
