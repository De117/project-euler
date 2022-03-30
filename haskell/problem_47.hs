-- Problem 47 (Distinct primes factors)
-- ====================================
--
-- The first two consecutive numbers to have two distinct prime factors are:
--
--     14 = 2 × 7
--     15 = 3 × 5
--
-- The first three consecutive numbers to have three distinct prime factors are:
--
--     644 = 2² × 7 × 23
--     645 = 3 × 5 × 43
--     646 = 2 × 17 × 19.
--
-- Find the first four consecutive integers to have four distinct prime factors
-- each. What is the first of these numbers?
import Common (primes, decompose, toList)

numPrimeFactors :: (Integral a) => a -> Int
numPrimeFactors = length . toList . decompose

findFirst :: (Integral a) => [(a, a)] -> a
findFirst ((a,i1):(b,i2):(c,i3):(d,i4):rest)
    | all (==4) [i1, i2, i3, i4] = a
    | otherwise                  = findFirst ((b,i2):(c,i3):(d,i4):rest)


main = print . findFirst . zip [1..] $ map numPrimeFactors [1..]
