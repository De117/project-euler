-- Problem 40 (Champernowne's constant)
--
-- An irrational decimal fraction is created by concatenating the
-- positive integers:
--
--     0.123456789101112131415161718192021...
--
-- It can be seen that the 12th digit of the fractional part is 1.
--
-- If dn represents the nth digit of the fractional part, find the
-- value of the following expression.
--
--    d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000
import Data.Char (ord)

champernowne = concat (map show [1..])
digits = [champernowne !! (10^i - 1) | i <- [0..6]]
main = print $ product (map (\c -> ord c - ord '0') digits)
