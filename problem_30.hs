-- Problem 30 (Digit fifth powers)
-- ===============================
--
-- Surprisingly there are only three numbers that can be
-- written as the sum of fourth powers of their digits:
--
--     1634 = 1⁴ + 6⁴ + 3⁴ + 4⁴
--     8208 = 8⁴ + 2⁴ + 0⁴ + 8⁴
--     9474 = 9⁴ + 4⁴ + 7⁴ + 4⁴
--
-- As 1 = 1⁴ is not a sum it is not included.
--
-- The sum of these numbers is 1634 + 8208 + 9474 = 19316.
--
-- Find the sum of all the numbers that can be written as
-- the sum of fifth powers of their digits.
--
-- Obviously, we cannot go through *all* numbers.
-- We have to have a stopping criterion.
--
--    N ≤ num_digits(N) * 9⁵
--
-- This holds for a given number of digits. But how many digits
-- is too many?
--
-- A k-digit number must be smaller than k * 9⁴. Since a k-digit number
-- is necessarily N < 10^k, we look for the first k where:
--
--    10**k > k * 9⁵
--
-- For 4th powers, this is 5 digits. (So N < 10⁵).
-- For 5th powers, this is 6 digits. (So N ≤ 10⁶).
import Data.Char (digitToInt)

digits :: (Show a, Integral a) => a -> [Int]
digits = map digitToInt . show

main = print (sum (filter (\n -> n == sum (map (^5) (digits n))) [2..10^6]))
