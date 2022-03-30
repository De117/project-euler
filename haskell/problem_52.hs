-- Problem 52 (Permuted multiples)
-- ===============================
--
-- It can be seen that the number, 125874, and its double, 251748,
-- contain exactly the same digits, but in a different order.
--
-- Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x,
-- and 6x, -- contain the same digits.
import Data.List (sort)
import Common (digits)

permutationsOfEachOther :: [Int] -> Bool
permutationsOfEachOther = allEqual . map (sort . digits)
    where
        allEqual [] = True
        allEqual (x:xs) = all (==x) xs

main = print . head . head . dropWhile (not . permutationsOfEachOther) $ multiples
    where
        multiples = [[x, 2*x, 3*x, 4*x, 5*x, 6*x] | x <- [1..]]
