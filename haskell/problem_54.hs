-- Problem 54 (Poker hands)
-- ========================
--
-- In the card game poker, a hand consists of five cards and are ranked,
-- from lowest to highest, in the following way:
--
--   * High Card:       Highest value card.
--   * One Pair:        Two cards of the same value.
--   * Two Pairs:       Two different pairs.
--   * Three of a Kind: Three cards of the same value.
--   * Straight:        All cards are consecutive values.
--   * Flush:           All cards of the same suit.
--   * Full House:      Three of a kind and a pair.
--   * Four of a Kind:  Four cards of the same value.
--   * Straight Flush:  All cards are consecutive values of same suit.
--   * Royal Flush:     Ten, Jack, Queen, King, Ace, in same suit.
--
-- The cards are valued in the order:
-- 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
--
-- If two players have the same ranked hands then the rank made up of the
-- highest value wins; for example, a pair of eights beats a pair of fives
-- (see example 1 below). But if two ranks tie, for example, both players
-- have a pair of queens, then highest cards in each hand are compared
-- (see example 4 below); if the highest cards tie then the next highest
-- cards are compared, and so on.
--
-- Consider the following five hands dealt to two players:
--
-- Hand       Player 1            Player 2          Winner
--
--   1     5H 5C 6S 7S KD      2C 3S 8S 8D TD      Player 2
--          Pair of Fives      Pair of Eights
--
--   2     5D 8C 9S JS AC      2C 5C 7D 8S QH      Player 1
--        Highest card Ace   Highest card Queen
--
--   3     2D 9C AS AH AC      3D 6D 7D TD QD      Player 2
--           Three Aces      Flush with Diamonds
--
--   4     4D 6S 9H QH QC      3D 6D 7H QD QS      Player 1
--         Pair of Queens      Pair of Queens
--        Highest card Nine  Highest card Seven
--
--   5     2H 2D 4C 4D 4S      3C 3D 3S 9S 9D      Player 1
--          Full House           Full House
--        With Three Fours    with Three Threes
--
--
-- The file, poker.txt, contains one-thousand random hands dealt to two players.
-- Each line of the file contains ten cards (separated by a single space):
-- the first five are Player 1's cards and the last five are Player 2's cards.
-- You can assume that all hands are valid (no invalid characters or repeated
-- cards), each player's hand is in no specific order, and in each hand there
-- is a clear winner.
--
-- How many hands does Player 1 win?


-- Implementing poker requires no math, but it does take a bit of code.
-- For a start, we need to model our domain.

import Data.Ord (comparing)
import Data.List (sort, group)
import Data.Maybe (catMaybes)
import Control.Monad (forM_)

data Suit = Hearts | Diamonds | Clovers | Spades
    deriving (Eq)

instance Show Suit where
    show Hearts   = "H"
    show Diamonds = "D"
    show Clovers  = "C"
    show Spades   = "S"

data Strength = Two
          | Three
          | Four
          | Five
          | Six
          | Seven
          | Eight
          | Nine
          | Ten
          | Jack
          | Queen
          | King
          | Ace
     deriving (Eq, Ord, Enum, Bounded)

instance Show Strength where
    show Two   = "2"
    show Three = "3"
    show Four  = "4"
    show Five  = "5"
    show Six   = "6"
    show Seven = "7"
    show Eight = "8"
    show Nine  = "9"
    show Ten   = "T"
    show Jack  = "J"
    show Queen = "Q"
    show King  = "K"
    show Ace   = "A"

data Card = Card {cardStrength :: Strength, cardSuit :: Suit} deriving (Eq)

instance Show Card where
    show c = show (cardStrength c) ++ show (cardSuit c)

instance Ord Card where
    compare = comparing cardStrength

newtype Hand = Hand [Card] deriving (Eq, Show)

fromList :: [Card] -> Hand
fromList = Hand . sort 


-- A rank has all the information needed to break ties between two same,
-- but not equal ranks. In the general case, it's a big-endian list of card
-- strengths. For example, a FullHouse of three 7s and two 4s is represented
-- as FullHouse [Seven, Four].
-- List comparison ensures that the more important parts (three cards) will
-- be treated as more important.

data Rank = HighCard [Strength]
               | OnePair Strength
               | TwoPairs [Strength]
               | ThreeOfAKind Strength
               | Straight Strength
               | Flush
               | FullHouse [Strength]
               | FourOfAKind Strength
               | StraightFlush Strength
               | RoyalFlush
                deriving (Eq, Ord, Show)


-- Then, a big-endian list of these ranks provides everything needed to
-- characterize the strength of a whole hand, and resolve any rank ties.

-- | Results, ordered from best to worst.
results :: Hand -> [Rank]
results h = catMaybes [ royalFlush    h
                      , straightFlush h
                      , fourOfAKind   h
                      , fullHouse     h
                      , flush         h
                      , straight      h
                      , threeOfAKind  h
                      , twoPairs      h
                      , onePair       h
                      , highCard      h
                      ]

leftWins :: Hand -> Hand -> Bool
leftWins h1 h2 = (results h1) > (results h2)

--------------------------------------------------------------------------------

-- Here we have a list of functions to detect ranks in a hand.

highCard :: Hand -> Maybe Rank
highCard (Hand h) = Just . HighCard . reverse . sort . map cardStrength $ h

onePair :: Hand -> Maybe Rank
onePair (Hand h)
    | null groupsOfTwo = Nothing
    | otherwise        = Just . OnePair . head . head $ groupsOfTwo
    where
        groupsOfTwo = filter ((==2) . length) . group . map cardStrength $ h

twoPairs :: Hand -> Maybe Rank
twoPairs (Hand h)
    | length groupsOfTwo < 2 = Nothing
    | otherwise              = Just (TwoPairs [better, worse])
    where
        better = max (groupsOfTwo !! 0 !! 0) (groupsOfTwo !! 1 !! 0)
        worse  = min (groupsOfTwo !! 0 !! 0) (groupsOfTwo !! 1 !! 0)
        groupsOfTwo = filter ((==2) . length) . group . map cardStrength $ h

threeOfAKind :: Hand -> Maybe Rank
threeOfAKind (Hand h)
    | null groupsOfThree = Nothing
    | otherwise          = Just . ThreeOfAKind . head . head $ groupsOfThree
    where
        groupsOfThree = filter ((==3) . length) . group . map cardStrength $ h

straight :: Hand -> Maybe Rank
straight (Hand h)
    | consecutive strengths = Just . Straight . maximum $ strengths
    | otherwise             = Nothing
    where
        strengths = map cardStrength h

flush :: Hand -> Maybe Rank
flush (Hand h)
    | all (==suit) (map cardSuit h)  = Just Flush
    | otherwise                      = Nothing
    where
        suit = cardSuit (head h)

fullHouse :: Hand -> Maybe Rank
fullHouse h = case (onePair h, threeOfAKind h) of
                (Just (OnePair s1), Just (ThreeOfAKind s2)) -> Just (FullHouse [s2, s1])
                _                                           -> Nothing

fourOfAKind :: Hand -> Maybe Rank
fourOfAKind (Hand h)
    | null groupsOfFour = Nothing
    | otherwise          = Just . FourOfAKind . head . head $ groupsOfFour
    where
        groupsOfFour = filter ((==4) . length) . group . map cardStrength $ h

straightFlush :: Hand -> Maybe Rank
straightFlush h = case (straight h, flush h) of
                    (Just (Straight s), Just Flush) -> Just (StraightFlush s)
                    _                               -> Nothing

royalFlush :: Hand -> Maybe Rank
royalFlush h = case straightFlush h of
                    Just (StraightFlush Ace) -> Just RoyalFlush
                    _                        -> Nothing


consecutive :: (Enum a, Ord a) => [a] -> Bool
consecutive [] = True
consecutive [x] = True
consecutive (x:y:xs) = (x < y) && (x == pred y) && consecutive (y:xs)


-- File parsing code
--------------------

parseStrength :: Char -> Strength
parseStrength '2' = Two
parseStrength '3' = Three
parseStrength '4' = Four
parseStrength '5' = Five
parseStrength '6' = Six
parseStrength '7' = Seven
parseStrength '8' = Eight
parseStrength '9' = Nine
parseStrength 'T' = Ten
parseStrength 'J' = Jack
parseStrength 'Q' = Queen
parseStrength 'K' = King
parseStrength 'A' = Ace

parseSuit :: Char -> Suit
parseSuit 'H' = Hearts
parseSuit 'D' = Diamonds
parseSuit 'C' = Clovers
parseSuit 'S' = Spades

parseLine :: String -> (Hand, Hand)
parseLine l = (fromList (map parseElement player1), fromList (map parseElement player2))
    where
        player1 = take 5 . words $ l
        player2 = take 5 . drop 5 . words $ l
        parseElement [c1, c2] = Card (parseStrength c1) (parseSuit c2)

--------------------------------------------------------------------------------

main = do
    contents <- readFile "p054_poker.txt"
    let games = map parseLine (lines contents)
    print . sum . map (fromEnum . uncurry leftWins) $ games
