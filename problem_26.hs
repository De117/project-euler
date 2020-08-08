-- Problem 26 (Reciprocal cycles)
-- ==============================
--
-- A unit fraction contains 1 in the numerator. The decimal representation
-- of the unit fractions with denominators 2 to 10 are given:
--
--     1/2 =   0.5
--     1/3 =   0.(3)
--     1/4 =   0.25
--     1/5 =   0.2
--     1/6 =   0.1(6)
--     1/7 =   0.(142857)
--     1/8 =   0.125
--     1/9 =   0.(1)
--     1/10    =   0.1
--
-- Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
-- It can be seen that 1/7 has a 6-digit recurring cycle.
--
-- Find the value of d < 1000 for which 1/d contains the longest
-- recurring cycle in its decimal fraction part.
import Data.Ord (comparing)
import Data.List (findIndex, maximumBy)


-- Divides 1 by n.
-- Returns: (decimals, cycleLength)
divide1By :: Int -> ([Int], Int)
divide1By n = divide' n 10 [] [1]
    where
        divide' _ 0 decimals _                 = (decimals, 0)  -- Terminal case, nothing to divide.
        divide' n dividend decimals remainders =
            let
                decimal   = dividend `div` n
                remainder = dividend `mod` n
                decimals' = decimals ++ [decimal]
                remainders' = remainders ++ [remainder]
            in
            case (findIndex (==remainder) remainders)
            of Nothing -> divide' n (10*remainder) decimals' remainders'  -- Keep dividing.
               Just i -> (
                -- We've hit a cycle!
                let cycleLength = (length remainders' - 1) - i
                in (decimals', cycleLength))


-- Select maximum element from list, according to value provided by applying `f`.
--
-- Normally, this would by `maximumBy (comparing f)`... but that, for some reason,
-- is much slower, with 2x more evaluations of `f` than needed.
maxBy :: (Ord b) => (a -> b) -> [a] -> a
maxBy f = fst . maximumBy (comparing snd) . map (\x -> (x, f x))


main = print $ maxBy (snd . divide1By) [1..999]
