-- Coin sums (Problem 31)
-- ======================
--
-- In the United Kingdom the currency is made up of pound (£) and pence (p).
-- There are eight coins in general circulation:
--
--     1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
--
-- It is possible to make £2 in the following way:
--
--     1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
--
-- How many different ways can £2 be made using any number of coins?


-- We have a bag to fill. In how many ways can we fill it?
items = [200, 100, 50, 20, 10, 5, 2, 1]

-- We can fit up to X₁ of item x₁, up to X₂ of item x₂, and so on.
-- We could just try out all values for the vector [x₁, ... , x_n],
-- bounded above by [X₁, ... X_n], but that is still slow & inefficient.
-- Because, once we add an element, the bounds for all other elements go
-- down, and the absolute bound is then way too loose.
--
-- So: we put in up to X₁ of x₁, and then recursively solve the rest.
--
-- It works better if we start with the biggest items first, because if
-- there's no combination possible with the given items & their counts,
-- we try out less combinations before concluding that it's not possible.

ways :: [Int] -> Int -> [[Int]]
ways _  0  = [[]]  -- Just one way to fill nothing
ways [] _  = []    -- No way to fill anything without items
ways (item:items) space = [replicate n item ++ way |
                                n <- [0..bound],
                                way <- ways items (space - n*item)]
    where
        bound = space `div` item  -- See how many times can we fit the item in


main = print . length . ways items $ 200
