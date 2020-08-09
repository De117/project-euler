-- Problem 37 (Truncatable primes)
-- ===============================
--
-- The number 3797 has an interesting property. Being prime itself, it is
-- possible to continuously remove digits from left to right, and remain
-- prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
-- right to left: 3797, 379, 37, and 3.
--
-- Find the sum of the only eleven primes that are both truncatable from
-- left to right and right to left.
--
-- NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
import Common (primes, isPrime, digits, fromDigits)

leftToRight  :: (Integral a) => a -> Bool
leftToRight p = all isPrime [fromDigits $ drop i ds | i <- [0..length ds-1]]
    where ds = (digits p)

rightToLeft :: (Integral a) => a -> Bool
rightToLeft p = all isPrime [fromDigits $ take i ds | i <- [1..length ds]]
    where ds = (digits p)

isTruncatable p = leftToRight p && rightToLeft p


main = print . sum . take 11 . drop 4 . filter isTruncatable $ (primes :: [Int])
