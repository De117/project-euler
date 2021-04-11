-- Problem 53 (Combinatoric selections)
-- ====================================
--
-- There are exactly ten ways of selecting three from five, 12345:
--
--   123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
--
-- In combinatorics, we use the notation, (5 over 3) = 10.
--
-- In general, (n over r) = n! / r!(n-r)!,
--
-- where r ≤ n,
--       n! = n × (n-1) × ... × 3 × 2 × 1,
--   and 0! = 1.
--
-- It is not until n = 23, that a value exceeds one-million: (23 over 10) = 1144066.
--
-- How many, not necessarily distinct, values of (n over r) for 1 ≤ n ≤ 100,
-- are greater than one-million?
import Data.List (foldl')

fact :: Integral a => a -> a
fact n = foldl' (*) 1 [1..n]

over :: Integral a => a -> a -> a
n `over` k = (fact n) `div` (fact k * fact (n-k))

main = print . length $ filter (>10^6) [n `over` k | n <- [1..100], k <- [1..n]]
