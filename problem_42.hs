-- Problem 42 (Coded triangle numbers)
-- ===================================
--
-- The nth term of the sequence of triangle numbers is given by, t_n = ½n(n+1);
-- so the first ten triangle numbers are:
--
--     1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
--
-- By converting each letter in a word to a number corresponding to its
-- alphabetical position and adding these values we form a word value. For
-- example, the word value for SKY is 19 + 11 + 25 = 55 = t_10. If the word
-- value is a triangle number then we shall call the word a triangle word.
--
-- Using words.txt (right click and 'Save Link/Target As...'), a 16K text
-- file containing nearly two-thousand common English words, how many are
-- triangle words?
import Data.Text (pack, unpack, split)
import Data.Char (ord)

-- A triangle number is of shape n = k(k+1)/2.
-- From here,
--     k² + k - 2n = 0
--     k = (-1 +- sqrt(1+8n))/2  -> ought to be integral
--
isTriangular :: (Integral a) => a -> Bool
isTriangular n = k > 0 && isIntegral k
    where
        k = (-1 + sqrt (fromIntegral (1 + 8*n))) / 2
        isIntegral x = abs (x - fromIntegral (round x)) < 1e-14

value :: String -> Int
value word = sum [ord c - ord 'A' + 1 | c <- word]

main = do
    contents <- readFile "p042_words.txt"
    -- split on commas, trim quotes
    let splat = map unpack $ split (==',') (pack contents)
    let words = map (filter (/='"')) splat
    print . length . filter isTriangular . map value $ words
