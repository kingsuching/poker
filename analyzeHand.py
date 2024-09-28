import os
import sys
from contextlib import contextmanager, suppress
import pandas as pd
from Board import Board
from Card import Card
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
    hand = Hand()
    board = Board()
    hand.cards = [Card('10', 'Hearts'), Card('9', 'Diamonds')]
    board.setCards([
        Card('8', 'Clubs'),
        Card('7', 'Spades'),
        Card('3', 'Hearts'),
    ])
    result = analyzeHand(hand, board)
    print(result)