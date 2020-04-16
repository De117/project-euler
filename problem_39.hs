-- Problem 39 (Integer right triangles)
-- ====================================
--
-- If p is the perimeter of a right angle triangle with integral length
-- sides, {a,b,c}, there are exactly three solutions for p = 120.
--
-- {20,48,52}, {24,45,51}, {30,40,50}
--
-- For which value of p ≤ 1000, is the number of solutions maximised?
--
import Data.List (maximumBy)
import Data.Ord (comparing)

isRightTriangle :: Integral a => (a, a, a) -> Bool
isRightTriangle (a, b, c) = a^2 + b^2 == c^2

solutions :: Integral a => a -> [(a, a, a)]
solutions p = filter isRightTriangle [(a, b, c) | a <- [1..p - 2],
                                                  b <- [1..p - 2 - a],
                                                  let c = p - a - b]

(p, _) = maximumBy (comparing (length . snd)) [(p, solutions p) | p <- [1..1000]]

main = print (p :: Int)
