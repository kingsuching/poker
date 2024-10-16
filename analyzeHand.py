import os
import sys
from contextlib import contextmanager
import pandas as pd
from tqdm import tqdm
from Board import Board
from Card import Card
from Deck import Deck
from Hand import Hand
from Player import Player
from PokerHandCheck import check, standardize


@contextmanager
def suppress_output():
    with open(os.devnull, 'w') as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout


def analyzeHand(hand, board=None, n=100, players=5):
    """
    :param hand: Hand of Cards
    :param board: current state of the board
    :param n: number of simulations
    :return: probability of each type of hand after n simulations
    """

    types = []
    boardCopy = Board()
    for i in range(players-1):
        plyr = Player("CPU Player " + str(i+1))
        plyr.hand = Hand()
    if board is not None:
        boardCopy.cards = board.cards.copy()

    for i in tqdm(range(n)):
        with suppress_output():
            boardCopy.flop()
            boardCopy.turn()
            boardCopy.river()
            result = check(hand, boardCopy)
            types.append(result)
            boardCopy.cards = board.cards.copy()

    series = pd.Series(types)
    return series.value_counts(normalize=True).round(3)

def parse_card(row):
    standardizedSuit = standardize(row['Suit'])
    return Card(str(row['Rank']), standardizedSuit)

if __name__ == '__main__':
    global_deck = Deck(True)
    read = False
    csv = True

    if csv:
        hand = Hand(False)
        board = Board()
        handStrings = pd.read_excel('handAndBoard.xlsx', sheet_name='Hand')
        boardStrings = pd.read_excel('handAndBoard.xlsx', sheet_name='Board')
        handCards = handStrings.apply(parse_card, axis=1).tolist()
        boardCards = boardStrings.apply(parse_card, axis=1).tolist()
        hand.setCards(handCards)
        board.setCards(boardCards)
        result = analyzeHand(hand, board)
        guarantee = check(hand, board)
        print("Guaranteed: ", guarantee)
        print(result)
        exit(0)

    if read:
        hand = Hand(False)
        board = Board()
        count = 0
        with open('handAndBoard.txt', 'r') as file:
            for line in file:
                if count == 0:
                    tokens = line.split(": ")[1].split(", ")
                    card1 = Card(tokens[0].split()[0], standardize(tokens[0].split()[2]))
                    card2 = Card(tokens[1].split()[0], standardize(tokens[1].split()[2]))
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
        guarantee = check(hand, board)
        print("Guaranteed: ", guarantee)
        print(result)
        exit(0)

    handCards = input("Enter hand cards in the following format: 9 of Hearts, 10 of Diamonds. Case doesn't matter\n")
    handCards = handCards.split(", ")
    if len(handCards) != 2:
        raise ValueError("Please enter 2 cards")
    card1 = Card(handCards[0].split()[0], standardize(handCards[0].split()[2]))
    card2 = Card(handCards[1].split()[0], standardize(handCards[1].split()[2]))

    boardCards = input("Enter board cards in the following format: 9 of Hearts, 10 of Diamonds, etc. up to 4 cards\n")
    boardCards = boardCards.split(", ")
    bc = []
    if len(boardCards) >= 5:
        raise ValueError(f"Please enter up to 4 cards. Got {len(boardCards)}")
    for cardString in boardCards:
        card = Card(cardString.split()[0], cardString.split()[2])
        bc.append(card)
    hand = Hand(False)
    board = Board()
    hand.setCards([card1, card2])
    board.setCards(bc)
    result = analyzeHand(hand, board)
    guarantee = check(hand, board)
    print("Guaranteed: ", guarantee)
    print(result)