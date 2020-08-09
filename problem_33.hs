-- Problem 33 (Digit cancelling fractions)
-- =======================================
--
-- The fraction 49/98 is a curious fraction, as an inexperienced mathematician
-- in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which
-- is correct, is obtained by cancelling the 9s.
--
-- We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
--
-- There are exactly four non-trivial examples of this type of fraction,
-- less than one in value, and containing two digits in the numerator
-- and denominator.
--
-- If the product of these four fractions is given in its lowest common
-- terms, find the value of the denominator.

isCurious :: (Int, Int) -> Bool
isCurious (numerator, denominator)
    | n1 == d2 && d1 /= 0 && (n2 / d1) == fraction = True
    | n2 == d1 && d2 /= 0 && (n1 / d2) == fraction = True
    | n1 == d1 && d2 /= 0 && (n2 / d2) == fraction = True
    | otherwise = False
    where
        n1 = realToFrac $ numerator `div` 10
        n2 = realToFrac $ numerator `mod` 10
        d1 = realToFrac $ denominator `div` 10
        d2 = realToFrac $ denominator `mod` 10
        fraction = (realToFrac numerator) / (realToFrac denominator)

-- multiply fractions
mul :: (Int, Int) -> (Int, Int) -> (Int, Int)
mul (n1,d1) (n2, d2) = (n1*n2, d1*d2)

-- simplify fraction
simplify :: (Int, Int) -> (Int, Int)
simplify (numerator, denominator) = (numerator `div` g, denominator `div` g)
    where
        g = gcd numerator denominator

main = print . snd . simplify . foldl1 mul $ curious
    where
        curious = filter isCurious $ [(i,j) | j <- [10..99], i <- [10..j-1]]
