-- Problem 57 (Square root convergents)
-- ====================================
--
-- It is possible to show that the square root of two can be expressed
-- as an infinite continued fraction.
--
--                               1
--     sqrt(2) =  1   +   ------------------
--                         2 +       1
--                             -------------
--                             2 + 1/(2+...)
--
-- By expanding this for the first four iterations, we get:
--
--
--     1 + 1/2          = 3/2   = 1.5
--
--            1
--     1 + -------      = 7/5   = 1.4
--         2 + 1/2
--
--            1
--     1 + -----------  = 17/12 = 1.41666...
--         2 +   1
--             -------
--             2 + 1/2
--
--            1
--     1 + -------------  = 41/29 = 1.41379...
--         2 +   1
--             ---------
--             2 +  1
--                 -----
--                 2+1/2
--
-- The next three expansions are 99/70, 239/169, and 577/408, but the eighth
-- expansion, 1393/985, is the first example where the number of digits in
-- the numerator exceeds the number of digits in the denominator.
--
-- In the first one-thousand expansions, how many fractions
-- contain a numerator with more digits than the denominator?
import Common (digits)

data EF = Zero | EF {numerator :: Integer, ldenominator :: Integer, rdenominator :: EF}
        deriving (Eq, Show)

toFraction :: EF -> (Integer, Integer)
toFraction Zero = (0, 1)
toFraction (EF num ldenom Zero) = (num, ldenom)
toFraction (EF num ldenom rdenom) = let
    -- We have
    --         num
    --    --------------
    --    ldenom + r1/r2
    --
    (r1, r2) = toFraction rdenom
    --
    -- which simplifies to
    --
    in (r2*num, (r2*ldenom + r1))

-- In the general case, we might need to reduce the fraction by eliminating
-- any common factors of the resulting numerator and denominator.
-- But in our case ldenom is always 1, so there's no need.

expand :: EF -> EF
expand (EF num ldenom Zero)   = EF num ldenom (EF 1 2 Zero)
expand (EF num ldenom rdenom) = EF num ldenom (expand rdenom)

main = print . length . filter p . take 1000 . map (addOne . toFraction) . iterate expand $ oneHalf
    where
        oneHalf = EF 1 2 Zero
        addOne (num, denom) = (num + denom, denom)
        p (a, b) = length (digits a) > length (digits b)
