-- Problem 16 (Power digit sum)
-- ============================
--
-- 2¹⁵ = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
--
-- What is the sum of the digits of the number 2¹⁰⁰⁰?
import Common (digits)

main = print . sum . digits $ 2^1000
