-- Problem 46 (Goldbach's other conjecture)
-- ========================================
--
-- It was proposed by Christian Goldbach that every odd composite
-- number can be written as the sum of a prime and twice a square.
--
--     9 = 7 + 2×1²
--     15 = 7 + 2×2²
--     21 = 3 + 2×3²
--     25 = 7 + 2×3²
--     27 = 19 + 2×2²
--     33 = 31 + 2×1²
--
-- It turns out that the conjecture was false.
--
-- What is the smallest odd composite that cannot be written as
-- the sum of a prime and twice a square?
import qualified Data.IntMap as M
import Data.List (foldl')
import Common (primes, isPrime)

-- Presumably, most odd composites *can* be so written.
-- It should be efficient to sieve them out, and see what's left.


-- Each iteration of the sieve is bounded.
-- You can increase the bound as needed.
sieve :: Int -> Maybe Int
sieve upperBound = sieve' relevantPrimes initialState
    where
        relevantPrimes = takeWhile (<=upperBound) primes

        -- Create sieve, with even numbers marked off.
        initialState = M.fromList [(i, even i) | i <- [2..upperBound]]

        -- Step: mark off all composites based on the current prime.
        sieve' (p:ps) stateMap = sieve' ps newState
            where
                ub = ceiling . sqrt . fromIntegral $ (upperBound - p)
                toMarkOff = [p + 2*i*i | i <- [0..ub]]
                newState = foldl' (\m i -> M.insert i True m) stateMap toMarkOff

        -- When done sieving, find first number not marked off.
        sieve' [] stateMap = let m = M.filter (not . id) stateMap
            in if m == M.empty
               then Nothing
               else Just (head (M.keys m))


main = print . definitely . head . filter exists . map sieve . iterate (*2) $ 1000
    where
        exists Nothing  = False
        exists (Just x) = True
        definitely (Just x) = x
