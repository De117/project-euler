-- Problem 51 (Prime digit replacements)
-- =====================================
--
-- By replacing the 1st digit of the 2-digit number *3, it turns out that
-- six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
--
-- By replacing the 3rd and 4th digits of 56**3 with the same digit, this
-- 5-digit number is the first example having seven primes among the ten
-- generated numbers, yielding the family: 56003, 56113, 56333, 56443,
-- 56663, 56773, and 56993. Consequently 56003, being the first member
-- of this family, is the smallest prime with this property.
--
-- Find the smallest prime which, by replacing part of the number
-- (not necessarily adjacent digits) with the same digit, is part
-- of an eight prime value family.
import Common (digits, fromDigits, isPrime, primes)
import Data.List (maximumBy)
import Data.Ord (comparing)

-- Let's see... for each D-digit number, we have (D over 1) units, (D over 2)
-- pairs, (D over 3) triples, etc. for a total of
--
--     D-1
--      ∑  (D over i)
--     i=1
--
-- ways to select (replace) part of the number.
-- This just happens to be the sum of the D-th row of Pascal's triangle, minus
-- the first and last elements, and equal to 2^D - 2. Another explanation for
-- this is that it's all the subsets of the set of D digit( position)s, except
-- for the empty set and the set itself.
--
-- So, if the solution is a prime p, we can put an upper bound on the number
-- of subsets tried out:
--
--     π(p) * 2^⌈log₂(p)⌉ ≤ π(p) * (p+1) ≈ p²/ln p
--
-- Nearly quadratic, but then again, computers are fast these days.

main = print . minimum . head . dropWhile ((<8) . length) . map largestFamily $ primes


largestFamily :: Int -> [Int]
largestFamily n = case map (filter isPrime) (replaceDigits n) of
                    [] -> []
                    xs -> maximumBy (comparing length) xs


replaceDigits :: Int -> [[Int]]
replaceDigits n = concat [replaceKDigits i n | i <- [1..length (digits n)-1]]


-- | Replace k digits of n.
-- Returns all possible replacements.
-- First digit can never be replaced with zero.
replaceKDigits :: Int -> Int -> [[Int]]
replaceKDigits k n = [map fromDigits
                        [replace indices d ds | d <- if (head indices /= 0)
                                                     then [0..9]
                                                     else [1..9]]
                                              | indices <- setsOf k [0..length ds-1]]
    where
        ds = digits n

-- | Replace elements at specified indices with given element.
-- NB: doesn't behave well if index is out of bounds.
replace :: [Int] -> a -> [a] -> [a]
replace []     _ xs = xs
replace (i:is) e xs = let xs' = take i xs ++ [e] ++ drop (i+1) xs
                      in replace is e xs'

-- | All subsets of size k.
setsOf :: Integral a => a -> [b] -> [[b]]
setsOf _ []     = []
setsOf 0 _      = [[]]
setsOf 1 xs     = map pure xs
setsOf k (x:xs) = setsOf k xs ++ [x:xs' | xs' <- setsOf (k-1) xs]
