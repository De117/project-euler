-- Problem 17 (Number letter counts)
-- =================================
--
-- If the numbers 1 to 5 are written out in words: one, two, three, four,
-- five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
--
-- If all the numbers from 1 to 1000 (one thousand) inclusive were written
-- out in words, how many letters would be used?
--
-- NOTE: Do not count spaces or hyphens. For example, 342 (three hundred
--       and forty-two) contains 23 letters and 115 (one hundred and fifteen)
--       contains 20 letters. The use of "and" when writing out numbers is in
--       compliance with British usage.
import Data.Char (isAlpha)

ones n
    | n == 1 = "one"
    | n == 2 = "two"
    | n == 3 = "three"
    | n == 4 = "four"
    | n == 5 = "five"
    | n == 6 = "six"
    | n == 7 = "seven"
    | n == 8 = "eight"
    | n == 9 = "nine"

tens n
    | n < 10  = ones n
    | n == 10 = "ten"
    | n == 11 = "eleven"
    | n == 12 = "twelve"
    | n == 13 = "thirteen"
    | n == 14 = "fourteen"
    | n == 15 = "fifteen"
    | n == 16 = "sixteen"
    | n == 17 = "seventeen"
    | n == 18 = "eighteen"
    | n == 19 = "nineteen"
    | n == 20 = "twenty"
    | n == 30 = "thirty"
    | n == 40 = "forty"
    | n == 50 = "fifty"
    | n == 60 = "sixty"
    | n == 70 = "seventy"
    | n == 80 = "eighty"
    | n == 90 = "ninety"
    | otherwise = tens (n `div` 10 * 10) ++ "-" ++ ones (n `mod` 10)

hundreds n
    | n < 100          = tens n
    | n `mod` 100 == 0 = (ones (n `div` 100)) ++ " hundred"
    | otherwise        = hundreds (n `div` 100 * 100) ++ " and " ++ tens (n `mod` 100)


numbersAsWords = concat (map hundreds [1..999] ++ ["one thousand"])
main = print . sum . map (fromEnum . isAlpha) $ numbersAsWords
