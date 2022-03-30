-- Problem 23 (Non-abundant sums)
-- ==============================
--
-- A perfect number is a number for which the sum of its proper divisors is
-- exactly equal to the number. For example, the sum of the proper divisors
-- of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
-- number.
--
-- A number n is called deficient if the sum of its proper divisors is less
-- than n and it is called abundant if this sum exceeds n.
--
-- As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
-- number that can be written as the sum of two abundant numbers is 24. By
-- mathematical analysis, it can be shown that all integers greater than 28123
-- can be written as the sum of two abundant numbers. However, this upper limit
-- cannot be reduced any further by analysis even though it is known that the
-- greatest number that cannot be expressed as the sum of two abundant numbers
-- is less than this limit.
--
-- Find the sum of all the positive integers which cannot be written as the sum
-- of two abundant numbers.
import Common (properDivisors, decompose)
import qualified Data.Set as S

isAbundant n = sum (properDivisors (decompose n)) > n

abundantNumbers = S.fromList $ filter isAbundant [1..28123]  -- This subset is sufficient.

isAbundant' = (flip S.member) abundantNumbers  -- faster version of `isAbundant`

-- Check all pairs that sum to `a`
canBeWritten = [a | a <- [1..28123], b <- findFirst a [1..a-1]]
    where
        -- and break when first one is found
        -- (hence, no standard list comprehension)
        findFirst a [] = []
        findFirst a (b:bs)
            | isAbundant' b && isAbundant' (a-b)  = [b]
            | otherwise                           = findFirst a bs

cannotBeWritten = S.difference (S.fromList [1..28123]) (S.fromList canBeWritten)

main = do
    -- These three lines don't do anything, but they make this program run
    -- about 10 seconds faster, somehow.
    let x = seq (S.size abundantNumbers) ""
    let y = seq (length canBeWritten) ""
    putStr $ x ++ y

    -- This is the *actual* main function.
    print $ sum cannotBeWritten
