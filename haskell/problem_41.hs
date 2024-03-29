-- Problem 41 (Pandigital prime)
-- =============================
--
-- We shall say that an n-digit number is pandigital if it makes use of all
-- the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
-- and is also prime.
--
-- What is the largest n-digit pandigital prime that exists?
import Data.List (permutations)
import Common (isPrime, fromDigits)

nPandigitals :: Int -> [Int]
nPandigitals n = map fromDigits (permutations (take n [1,2,3,4,5,6,7,8,9]))

main = print . maximum . filter isPrime . concat $ [nPandigitals i | i <- [1..9]]
