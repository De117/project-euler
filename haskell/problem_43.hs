-- Sub-string divisibility
-- Problem 43
--
-- The number, 1406357289, is a 0 to 9 pandigital number because it is
-- made up of each of the digits 0 to 9 in some order, but it also has
-- a rather interesting sub-string divisibility property.
--
-- Let d1 be the 1st digit, d2 be the 2nd digit, and so on.
-- In this way, we note the following:
--
--     d2d3d4=406 is divisible by 2
--     d3d4d5=063 is divisible by 3
--     d4d5d6=635 is divisible by 5
--     d5d6d7=357 is divisible by 7
--     d6d7d8=572 is divisible by 11
--     d7d8d9=728 is divisible by 13
--     d8d9d10=289 is divisible by 17
--
-- Find the sum of all 0 to 9 pandigital numbers with this property.
import Data.List

pandigital_numbers :: [Int]
pandigital_numbers = [read n :: Int | n <- permutations "0123456789", head n /= '0']

in_triples :: [a] -> [(a,a,a)]
in_triples l
  | length l <= 2   = []
  | otherwise       = (l!!0, l!!1, l!!2) : in_triples (tail l)


p :: Int -> Bool
p n = all divisibleBy' (zip subnumbers primes)
    where
        -- Setting primes!!0 to 1 means we can skip the special case of d₁d₂d₃₁d₂d₃
        primes = [1,2,3,5,7,11,13,17,19,23]

        -- triples of digits
        subnumbers =  [read [d1,d2,d3] :: Int | (d1,d2,d3) <- (in_triples (show n))]

        divisibleBy' (a,b) = a `mod` b == 0

main = print (sum (filter p pandigital_numbers))
