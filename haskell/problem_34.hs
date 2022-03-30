-- Problem 34 (Digit factorials)
--
-- 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
--
-- Find the sum of all numbers which are equal to the sum of the factorial
-- of their digits.
--
-- Note: as 1! = 1 and 2! = 2 are not sums they are not included.


-- Again, we cannot go through *all* numbers. We need a stopping criterion.
--
-- When a new digit is added, the number grows (up to) elevenfold; meanwhile,
-- the sum of the digits' factorials grows by at most 9! (=362880). It follows
-- that the sum must, sooner or later, permanently fall behind the numbers.
--
-- The numbers overtake the sum's speed when going from 6 to 7 digits.
-- They completely overtake the sum when going from 7 to 8 digits, since
-- the largest possible sum there is 8*9! = 2903040, less than the smallest
-- possible number.
--
-- This gives us an upper bound.
factorial :: Integral a => a -> a
factorial n = product [1..n]

digits :: Integral a => a -> [a]
digits n = _digits n []
    where
        _digits 0 xs = xs
        _digits n xs = _digits (n `div` 10) ((n `mod` 10):xs)

isCurious :: Integral a => a -> Bool
isCurious n = n == sum (map factorial (digits n))

curiousNumbers :: [Int]
curiousNumbers = filter isCurious [3..2903040]

main = print (sum curiousNumbers)
