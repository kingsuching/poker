import os
import sys
from contextlib import contextmanager
import pandas as pd
from Board import Board
from Card import Card
from Deck import Deck
from Hand import Hand
from PokerHandCheck import check


@contextmanager
def suppress_output():
    with open(os.devnull, 'w') as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout


def analyzeHand(hand, board=None, n=100):
    """
    :param hand: Hand of Cards
    :param board: current state of the board
    :param n: number of simulations
    :return: probability of each type of hand after n simulations
    """

    types = []
    boardCopy = Board()
    if board is not None:
        boardCopy.cards = board.cards.copy()
    with suppress_output():
        for i in range(n):
            boardCopy.flop()
            boardCopy.turn()
            boardCopy.river()
            result = check(hand, boardCopy)
            types.append(result)
            boardCopy.cards = board.cards.copy()

    series = pd.Series(types)
    return series.value_counts(normalize=True)

if __name__ == '__main__':
    global_deck = Deck(True)
    read = True

    if read:
        hand = Hand(False)
        board = Board()
        count = 0
        with open('handAndBoard.txt', 'r') as file:
            for line in file:
                if count == 0:
                    tokens = line.split(": ")[1].split(", ")
                    card1 = Card(tokens[0].split()[0], tokens[0].split()[2])
                    card2 = Card(tokens[1].split()[0], tokens[1].split()[2])
                    hand.setCards([card1, card2])
                elif count == 1:
                    tokens = line.split(": ")[1].split(", ")
                    bc = []
                    for cardString in tokens:
                        card = Card(cardString.split()[0], cardString.split()[2])
                        bc.append(card)
                    board.setCards(bc)
                count += 1
        result = analyzeHand(hand, board)
        print(result)
        exit(0)


    handCards = input("Enter hand cards in the following format: 9 of Hearts, 10 of Diamonds\n")
    handCards = handCards.split(", ")
    if len(handCards) != 2:
        raise ValueError("Please enter 2 cards")
    card1 = Card(handCards[0].split()[0], handCards[0].split()[2])
    card2 = Card(handCards[1].split()[0], handCards[1].split()[2])

    boardCards = input("Enter board cards in the following format: 9 of Hearts, 10 of Diamonds, etc. up to 4 cards\n")
    boardCards = boardCards.split(", ")
    bc = []
    if len(boardCards) >= 5:
        raise ValueError("Please enter up to 4 cards ONLY")
    for cardString in boardCards:
        card = Card(cardString.split()[0], cardString.split()[2])
        bc.append(card)
    hand = Hand(False)
    board = Board()
    hand.setCards([card1, card2])
    board.setCards(bc)

    """hand.cards = [Card('10', 'Hearts'), Card('9', 'Diamonds')]
    board.setCards([
        Card('8', 'Clubs'),
        Card('7', 'Spades'),
        Card('3', 'Hearts'),
    ])"""
    result = analyzeHand(hand, board)
    print(result)