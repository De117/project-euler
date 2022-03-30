-- Problem 19 (Counting Sundays)
-- =============================
--
-- You are given the following information,
-- but you may prefer to do some research for yourself.
--
--     1 Jan 1900 was a Monday.
--     Thirty days has September,
--     April, June and November.
--     All the rest have thirty-one,
--     Saving February alone,
--     Which has twenty-eight, rain or shine.
--     And on leap years, twenty-nine.
--     A leap year occurs on any year evenly divisible by 4,
--       but not on a century unless it is divisible by 400.
--
-- How many Sundays fell on the first of the month during
-- the twentieth century (1 Jan 1901 to 31 Dec 2000)?
import Common (divisibleBy)

isLeapYear :: Int -> Bool
isLeapYear y | y `divisibleBy` 400 = True
             | y `divisibleBy` 100 = False
             | y `divisibleBy` 4   = True
             | otherwise           = False

month :: Int -> Int -> Int
month y m | m == 2              = 28 + fromEnum (isLeapYear y)
          | m `elem` [4,6,9,11] = 30
          | otherwise           = 31


year :: Int -> Int
year y | isLeapYear y = 366
       | otherwise    = 365

data Weekday = Mon | Tue | Wed | Thu | Fri | Sat | Sun deriving (Eq, Enum, Show)

weekday :: Int -> Int -> Int -> Weekday
weekday y m d = toEnum (offset `mod` 7) :: Weekday
    where
        -- offset from 1900-01-01
        offset = offYears + offMonths + offDays
            where
                offYears  = sum (map year [1900..y - 1])
                offMonths = sum (map (month y) [1..m - 1])
                offDays   = d - 1


firstDays = [weekday y m 1 | y <- [1901..2000], m <- [1..12]]

main = print . length . filter (==Sun) $ firstDays
