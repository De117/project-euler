-- Problem 58 (Spiral primes)
-- ==========================
--
-- Starting with 1 and spiralling anticlockwise in the following way,
-- a square spiral with side length 7 is formed.
-- 
--    *37* 36  35  34  33  32 *31*
--     38  17  16  15  14 *13* 30
--     39  18  *5*  4  *3* 12  29
--     40  19   6   1   2  11  28
--     41  20  *7*  8   9  10  27
--     42  21  22  23  24  25  26
--    *43* 44  45  46  47  48  49
--
-- It is interesting to note that the odd squares lie along the bottom right
-- diagonal, but what is more interesting is that 8 out of the 13 numbers
-- lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.
--
-- If one complete new layer is wrapped around the spiral above, a square
-- spiral with side length 9 will be formed. If this process is continued,
-- what is the side length of the square spiral for which the ratio of
-- primes along both diagonals first falls below 10%?

import Common (isPrime)

-- This is similar to problem 28.
-- 
-- To repeat: if the final diameter ("side length") has D elements in it,
-- the distance between two adjacent diagonal elements will be D - 1.
--
-- Adding a new layer adds 4*(D-1) elements, and increases diameter by 2.
--
-- Now, we could make a nice-looking implementation such as this one:
-- 
-- > -- copied from problem 28
-- > diameters = [3,5..]
-- > distances = concat [replicate 4 (d-1) | d <- diameters]
-- > diagonalElements = scanl (+) 1 distances
-- > --
--
-- > diag n = take (1 + 4*n) diagonalElements
-- > avg l = (sum l) / fromIntegral (length l)
-- > percentage = avg . map (fromEnum . isPrime) . diag
-- 
-- And get a result like so:
-- > fst . head dropWhile ((>=0.10) . snd) . zip [1..] . map percentage $ [1..]
--
-- but this is not efficient. For an *efficient* implementation, we cannot go
-- over the whole list every time to calculate the percentage. We just need to
-- do it once, and keep totals of where we are.

find :: Int -> Int -> Int -> Int -> Int
find numPrimes numElements point layer
    | ratio >= 0.1 = find numPrimes' numElements' (last diagPoints) (layer + 1)
    | otherwise    = diameter  -- the "side length" we're looking for
    where
        diameter = 2 * layer + 1
        distance = diameter - 1
        diagPoints = take 4 . tail $ iterate (+distance) point
        numElements' = numElements + 4
        numPrimes' = numPrimes + sum [1 | _ <- filter isPrime diagPoints]
        ratio = fromIntegral numPrimes' / fromIntegral numElements'

main = print $ find 0 1 1 1
