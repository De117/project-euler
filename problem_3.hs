-- Problem 3 (Largest prime factor)
-- ================================
--
-- The prime factors of 13195 are 5, 7, 13 and 29.
--
-- What is the largest prime factor of the number 600851475143 ?
import Common (isPrime, divides)

primeFactors :: (Integral a) => a -> [a]
primeFactors n = filter isPrime . filter (`divides` n) $ [1..upperBound]
    where
        upperBound = ceiling (sqrt (fromIntegral n))

main = print . maximum $ primeFactors 600851475143
