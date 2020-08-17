-- Problem 50 (Consecutive prime sum)
-- ==================================
--
-- The prime 41, can be written as the sum of six consecutive primes:
--     41 = 2 + 3 + 5 + 7 + 11 + 13
--
-- This is the longest sum of consecutive primes that adds to a prime below
-- one-hundred.
--
-- The longest sum of consecutive primes below one-thousand that adds to a
-- prime, contains 21 terms, and is equal to 953.
--
-- Which prime, below one-million, can be written as the sum of the most
-- consecutive primes?
import Common (primes, isPrime)
import Data.Ord (comparing)
import Data.List (maximumBy)
import qualified Data.Map as M

limit = 10^6

primesBelow1M = takeWhile (<limit) primes

type Run = [Int]

-- The solution is, basically, a nested loop.
-- The only way to get reasonable performance is to break out of the inner loop
-- early. This means filtering won't do -- takeWhile will.
--
-- I'm using a map to keep state.
--
innerLoop :: Int -> M.Map Int Run -> M.Map Int Run
innerLoop i sums_adding_up_to = updated
    where
        -- First, we have the subset from which we'll be taking our runs.
        toCheck = drop i primesBelow1M

        -- Now, we don't really want to check _all_ runs.
        -- Just those which sum to a prime below the limit.
        runs :: [Run]
        runs = map (\(j, _) -> take j toCheck) . takeWhile ((<limit) . snd) $ zip [1..] partialSums
        partialSums = scanl1 (+) toCheck

        -- We check which ones sum to a prime, and add them to the map.
        updated :: M.Map Int Run
        updated = foldl f dict runs
            where
                f :: M.Map Int Run -> Run -> M.Map Int Run
                f acc run
                    | isPrime (sum run) = M.insertWith takeLonger (sum run) run acc
                    | otherwise         = acc
                dict = sums_adding_up_to
                takeLonger = \x y -> if length x > length y then x else y


-- The big loop is fairly straightforward.
runDict = foldl (\acc i -> innerLoop i acc) M.empty [0.._N]
    where
        _N = length primesBelow1M

main = print . fst . maximumBy (comparing (length . snd)) $ M.toList runDict
