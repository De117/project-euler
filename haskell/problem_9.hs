-- Problem 9 (Special Pythagorean triplet)
-- =======================================
--
-- A Pythagorean triplet is a set of three natural numbers, a < b < c,
-- for which,
--
--    a² + b² = c²
--
-- For example, 3² + 4² = 9 + 16 = 25 = 5².
--
-- There exists exactly one Pythagorean triplet for which a + b + c = 1000.
-- Find the product abc.
main = print $ head [ a*b*c  | a <- [1..1000],
                               b <- [1..1000],
                               let c = 1000 - a - b,
                               c > 0,
                               a^2 + b^2 == c^2]
