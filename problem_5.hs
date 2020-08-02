-- Problem 5 (Smallest multiple)
-- =============================
--
-- 2520 is the smallest number that can be divided by each of the numbers
-- from 1 to 10 without any remainder.
--
-- What is the smallest positive number that is evenly divisible by all
-- of the numbers from 1 to 20?
import Common (decompose, recompose, intersect)

main = print . recompose . foldl1 intersect . map decompose $ [1..20]
