import unittest
from Card import Card
from PokerHandCheck import check
from Board import Board
from Hand import Hand

class TestPokerHands(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.board.cards = [
            Card('10', 'Hearts'), Card('J', 'Hearts'), Card('Q', 'Hearts'),
            Card('K', 'Hearts'), Card('A', 'Hearts')
        ]

    def test_royal_flush(self):
        hand = Hand()
        hand.cards = [Card('10', 'Hearts'), Card('J', 'Hearts')]
        self.assertEqual('Royal Flush', check(hand, self.board))

    def test_straight_flush(self):
        hand = Hand()
        hand.cards = [Card('9', 'Hearts'), Card('8', 'Hearts')]
        self.board.cards = [
            Card('10', 'Hearts'), Card('J', 'Hearts'), Card('Q', 'Hearts'),
            Card('K', 'Hearts'), Card('7', 'Hearts')
        ]
        self.assertEqual('Straight Flush', check(hand, self.board))

    def test_four_of_a_kind(self):
        hand = Hand()
        hand.cards = [Card('10', 'Hearts'), Card('10', 'Diamonds')]
        self.board.cards = [
            Card('10', 'Clubs'), Card('10', 'Spades'), Card('2', 'Hearts'),
            Card('3', 'Hearts'), Card('4', 'Hearts')
        ]
        self.assertEqual('Four of a Kind', check(hand, self.board))

    def test_full_house(self):
        hand = Hand()
        hand.cards = [Card('10', 'Hearts'), Card('10', 'Diamonds')]
        self.board.cards = [
            Card('10', 'Clubs'), Card('3', 'Spades'), Card('3', 'Hearts'),
            Card('4', 'Hearts'), Card('5', 'Hearts')
        ]
        self.assertEqual('Full House', check(hand, self.board))

    def test_flush(self):
        hand = Hand()
        hand.cards = [Card('2', 'Hearts'), Card('4', 'Hearts')]
        self.board.cards = [
            Card('6', 'Hearts'), Card('8', 'Hearts'), Card('10', 'Hearts'),
            Card('J', 'Hearts'), Card('Q', 'Hearts')
        ]
        self.assertEqual('Flush', check(hand, self.board))

    def test_straight(self):
        hand = Hand()
        hand.cards = [Card('9', 'Hearts'), Card('8', 'Diamonds')]
        self.board.cards = [
            Card('10', 'Clubs'), Card('J', 'Spades'), Card('Q', 'Hearts'),
            Card('K', 'Hearts'), Card('7', 'Hearts')
        ]
        self.assertEqual('Straight', check(hand, self.board))

    def test_three_of_a_kind(self):
        hand = Hand()
        hand.cards = [Card('10', 'Hearts'), Card('10', 'Diamonds')]
        self.board.cards = [
            Card('10', 'Clubs'), Card('2', 'Spades'), Card('3', 'Hearts'),
            Card('4', 'Hearts'), Card('5', 'Hearts')
        ]
        self.assertEqual('Three of a Kind', check(hand, self.board))

    def test_two_pair(self):
        hand = Hand()
        hand.cards = [Card('10', 'Hearts'), Card('10', 'Diamonds')]
        self.board.cards = [
            Card('3', 'Clubs'), Card('3', 'Spades'), Card('4', 'Hearts'),
            Card('5', 'Hearts'), Card('6', 'Hearts')
        ]
        self.assertEqual('Two Pair', check(hand, self.board))

    def test_pair(self):
        hand = Hand()
        hand.cards = [Card('10', 'Hearts'), Card('1', 'Diamonds')]
        self.board.cards = [
            Card('2', 'Clubs'), Card('3', 'Spades'), Card('4', 'Hearts'),
            Card('10', 'Hearts'), Card('6', 'Hearts')
        ]
        self.assertEqual('Pair', check(hand, self.board))

    def test_high_card(self):
        hand = Hand()
        hand.cards = [Card('2', 'Hearts'), Card('4', 'Diamonds')]
        self.board.cards = [
            Card('6', 'Clubs'), Card('8', 'Spades'), Card('10', 'Hearts'),
            Card('J', 'Hearts'), Card('Q', 'Hearts')
        ]
        self.assertEqual('High Card', check(hand, self.board))

if __name__ == '__main__':
    unittest.main()