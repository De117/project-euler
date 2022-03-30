-- Problem 36 (Double-base palindromes)
-- ====================================
--
-- The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
--
-- Find the sum of all numbers, less than one million,
-- which are palindromic in base 10 and base 2.
--
-- (Please note that the palindromic number, in either base, may not include
-- leading zeros.)
isPalindrome :: Eq a => [a] -> Bool
isPalindrome s = (s == reverse s)

digitsInBase :: Integral a => a -> a -> [a]
digitsInBase base n = _digits base n []
    where
        _digits base 0 xs = xs
        _digits base n xs = _digits base (n `div` base) ((n `mod` base):xs)

isDoubleBasePalindrome :: Int -> Bool
isDoubleBasePalindrome i = isPalindrome (show i) && isPalindrome (digitsInBase 2 i)

main = print (sum (filter isDoubleBasePalindrome [1..1000000]))
