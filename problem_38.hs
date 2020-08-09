-- Problem 38 (Pandigital multiples)
-- =================================
--
-- Take the number 192 and multiply it by each of 1, 2, and 3:
--
--     192 × 1 = 192
--     192 × 2 = 384
--     192 × 3 = 576
--
-- By concatenating each product we get the 1 to 9 pandigital, 192384576.
-- We will call 192384576 the concatenated product of 192 and (1,2,3)
--
-- The same can be achieved by starting with 9 and multiplying by 1, 2, 3,
-- 4, and 5, giving the pandigital, 918273645, which is the concatenated
-- product of 9 and (1,2,3,4,5).
--
-- What is the largest 1 to 9 pandigital 9-digit number that can be formed
-- as the concatenated product of an integer with (1,2, ... , n) where n > 1?
import Data.List (permutations)
import Common (digits, fromDigits)

-- Only 362,880 numbers are 1 to 9 pandigital.
pandigitals = map fromDigits (permutations [1,2,3,4,5,6,7,8,9])

-- Since n > 1, and we have 9 digits, the largest starting number has ≤4 digits.
canBeFormed :: Int -> Bool
canBeFormed x = any (==x) [fromDigits (candidate i n) | i <- [1..4], n <- [1..nBound i]]
    where
        -- `i` is the length of the slice here.
        -- `n` is determined based on how many digits we take.
        nBound i = 9 `div` i
        ds = digits x

        -- Finally, this is the actual multiplication / concatenation part.
        candidate :: Int -> Int -> [Int]
        candidate i n = concat [digits (x * slice)  | x <- [1..n]]  -- may be longer than needed
            where
                slice = fromDigits (take i ds)


main = print . maximum . filter canBeFormed $ pandigitals
