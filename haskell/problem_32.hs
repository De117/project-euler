-- Problem 32 (Pandigital products)
-- ================================
--
-- We shall say that an n-digit number is pandigital if it makes use of all
-- the digits 1 to n exactly once; for example, the 5-digit number, 15234,
-- is 1 through 5 pandigital.
--
-- The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
-- multiplicand, multiplier, and product is 1 through 9 pandigital.
--
-- Find the sum of all products whose multiplicand/multiplier/product identity
-- can be written as a 1 through 9 pandigital.
--
-- HINT: Some products can be obtained in more than one way so be sure to only
-- include it once in your sum.
import Data.List (permutations)
import qualified Data.Set as S

-- The number of pandigital numbers is finite and reasonably small,
-- (in the millions), so we can just go through all of them, and check
-- which ones can be split into such a product.
--
-- Also, this definition of "pandigital" is slightly different than the
-- one in problem 47, so I'll call it "n-pandigital".

nPandigitalNumbers :: Int -> [[Int]]
nPandigitalNumbers n = permutations (take n [1,2,3,4,5,6,7,8,9])


-- We look for triples (a,b,p) such that a × b = p.
-- Can we split any n-pandigital number into such a triple?
-- The answer is no.
--
-- A product of a k-digit with an l-digit number will have r=(k+l) or r=(k+l-1)
-- digits. It follows that any split must be of the form k : l : r.
--
-- Let's generate all such splits.

splits :: Int -> [(Int, Int)]
splits n = filter isOK [(k, l) | k <- [1..n-2], l <- [1..n-2]]
    where
        isOK (k,l) = let r = (n-k-l) in (r == k+l || r == k+l-1)


slice :: Int -> Int -> [a] -> [a]
slice from toExclusive = drop from . take toExclusive

fromDigits :: Integral a => [a] -> a
fromDigits = foldl (\a b -> a*10+b) 0

-- And now, the actual check:
pandigitalTriples = [(a,b,p) |
        (k,l) <- splits 9,
        num <- nPandigitalNumbers 9,
        let a = fromDigits (slice 0 k num),
        let b = fromDigits (slice k (k+l) num),
        let p = fromDigits (slice (k+l) 10 num),
        a * b == p
    ]

pandigitalProducts = S.toList $ S.fromList [p | (a,b,p) <- pandigitalTriples]

main = print (sum pandigitalProducts)
