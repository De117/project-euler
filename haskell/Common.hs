module Common
( divisibleBy
, divides
, isPrime
, primes
, digits
, fromDigits
, decompose
, recompose
, intersect
, divisors
, properDivisors
, toList
) where

import Data.List (delete)


divisibleBy :: (Integral a) => a -> a -> Bool
divisibleBy a b = (a `mod` b) == 0

divides :: (Integral a) => a -> a -> Bool
divides = flip divisibleBy

isPrime :: (Integral a) => a -> Bool
isPrime n
    | n <= 1            = False
    | n <= 3            = True
    | even n            = False
    | otherwise         = not (any (`divides` n) [3,5..upperBound])
    where
        upperBound = ceiling (sqrt (fromIntegral n))

primes :: (Integral a) => [a]
primes = filter isPrime [1..]


digits :: Integral a => a -> [a]
digits n = _digits n []
    where
        _digits 0 xs = xs
        _digits n xs = _digits (n `div` 10) ((n `mod` 10):xs)

fromDigits :: Integral a => [a] -> a
fromDigits = foldl1 (\a b -> a*10 + b)



-------------------------------
-- Prime decomposition stuff --
-------------------------------

divisionArity :: (Integral a) => a -> a -> a
divisionArity n k = fromIntegral . length . takeWhile (`divisibleBy` k) . iterate (`div` k) $ n



data PrimeDecomposition a = PrimeDecomposition [(a, a)] deriving (Show, Eq)

decompose :: (Integral a) => a -> PrimeDecomposition a
decompose n
    | n < 1     = error "n must be >= 1!"
    | otherwise = PrimeDecomposition (decompose' n primes)
    where
        decompose' 1 _ = []
        decompose' n (p:primes')
            | n `divisibleBy` p  = (p, arity):decompose' (n `div` (p^arity)) primes'
            | otherwise          = decompose' n primes'
            where
                arity = divisionArity n p

-- Inverse of `decompose`
recompose :: (Integral a) => PrimeDecomposition a -> a
recompose = product . map (\(b, e) -> b^e) . unbox

unbox :: (Integral a) => PrimeDecomposition a -> [(a,a)]
unbox (PrimeDecomposition theList) = theList

add :: (Integral a) => PrimeDecomposition a -> PrimeDecomposition a -> PrimeDecomposition a
add x y = decompose ((recompose x) + (recompose y))

mul :: (Integral a) => PrimeDecomposition a -> PrimeDecomposition a -> PrimeDecomposition a
mul x y = PrimeDecomposition (mul' (unbox x) (unbox y))
    where
        mul' :: (Integral a) => [(a, a)] -> [(a, a)] -> [(a, a)]
        mul' xs [] = xs
        mul' [] ys = ys
        mul' (x@(p1,e1):xs) (y@(p2,e2):ys)
            | p1 == p2  = (p1, e1+e2):mul' xs ys
            | p1 < p2   = x:mul' xs (y:ys)
            | otherwise = y:mul' (x:xs) ys

intersect :: (Integral a) => PrimeDecomposition a -> PrimeDecomposition a -> PrimeDecomposition a
intersect x y = PrimeDecomposition (dot' (unbox x) (unbox y))
    where
        dot' xs [] = xs
        dot' [] ys = ys
        dot' (x@(p1,e1):xs) (y@(p2,e2):ys)
            | p1 == p2  = (p1, (max e1 e2)):dot' xs ys
            | p1 < p2   = x:dot' xs (y:ys)
            | otherwise = y:dot' (x:xs) ys


divisors :: (Integral a) => PrimeDecomposition a -> [a]
divisors (PrimeDecomposition []) = [1]
divisors (PrimeDecomposition (x:xs))
    | null xs   = factors x
    | otherwise = [f * d | f <- factors x, d <- divisors (PrimeDecomposition xs)]
    where
        factors (b, e) = [b^i | i <- [0..e]]


properDivisors :: (Integral a) => PrimeDecomposition a -> [a]
properDivisors n = delete (maximum divisorList) divisorList
    where
        divisorList = divisors n

-- for exporting
toList :: (Integral a) => PrimeDecomposition a -> [(a,a)]
toList = unbox
