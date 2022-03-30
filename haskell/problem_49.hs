-- Problem 49 (Prime permutations)
-- ===============================
--
-- The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
-- increases by 3330, is unusual in two ways: (i) each of the three terms
-- are prime, and, (ii) each of the 4-digit numbers are permutations of one
-- another.
--
-- There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
-- exhibiting this property, but there is one other 4-digit increasing sequence.
--
-- What 12-digit number do you form by concatenating the three terms in this
-- sequence?
import Common (primes, isPrime, digits, fromDigits)
import Data.List (permutations)

fourDigitPrimes = takeWhile (<10000) . dropWhile (<1000) $ primes

hasProperty p = isPrime a && a `elem` (permutations' p) &&
                isPrime c && c `elem` (permutations' p) &&
                length (digits a) == 4  -- a leading zero can disappear
    where
        permutations' = map fromDigits . permutations . digits
        a = p - 3330
        b = p
        c = p + 3330

sequences = map (\p -> [p - 3330, p, p+3330]) . filter hasProperty $ fourDigitPrimes

main = putStrLn . concat . map show . head . filter (not . elem 1487) $ sequences
