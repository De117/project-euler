-- Problem 35 (Circular primes)
--
-- The number, 197, is called a circular prime because all rotations
-- of the digits: 197, 971, and 719, are themselves prime.
--
-- There are thirteen such primes below 100:
-- 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
--
-- How many circular primes are there below one million?


-- Helper functions (mostly from problem 27):
-- =========================================
import Data.List (maximumBy)
import Data.Ord (comparing)


divisibleBy :: (Integral a) => a -> a -> Bool
divisibleBy a b = (a `mod` b) == 0

divides :: (Integral a) => a -> a -> Bool
divides = flip divisibleBy

isPrime :: (Integral a) => a -> Bool
isPrime n
    | n <= 1            = False
    | n <= 3            = True
    | n `divisibleBy` 2 = False
    | otherwise         = not (any (`divides` n) [3,5..upperBound])
    where
        upperBound = ceiling (sqrt (fromIntegral n))

primes :: (Integral a) => [a]
primes = filter isPrime [1..]


digits :: Integral a => a -> [a]
digits n = _digits n []
    where
        _digits :: Integral a => a -> [a] -> [a]
        _digits 0 xs = xs
        _digits n xs = _digits (n `div` 10) ((n `mod` 10):xs)


fromDigits :: Integral a => [a] -> a
fromDigits = foldl1 (\a b -> a*10 + b)

--
-- The actual solution:
--

rotations :: (Integral a) => a -> [a]
rotations n = [fromDigits (rotateLeft i asDigits) | i <- [0..length asDigits - 1]]
    where
        asDigits = digits n

        rotateLeft :: Int -> [a] -> [a]
        rotateLeft n xs = (drop n xs) ++ (take n xs)


isCircularPrime :: (Integral a) => a -> Bool
isCircularPrime p = all isPrime (rotations p)

-- We force p to an Int, because we don't need big integers
circular_primes = [p :: Int | p <- takeWhile (<10^6) primes, isCircularPrime p]

main = print (length circular_primes)
