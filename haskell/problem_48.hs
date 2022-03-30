-- Problem 48 (Self powers)
-- ========================
--
-- The series, 1¹ + 2² + 3³ + ... + 10¹⁰ = 10405071317.
--
-- Find the last ten digits of the series, 1¹ + 2² + 3³ + ... + 1000¹⁰⁰⁰.

takeLast n = reverse . take n . reverse

main = putStrLn . takeLast 10 . show . sum $ [i^i | i <- [1..1000]]
