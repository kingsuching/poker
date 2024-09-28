from random import random

import pandas as pd
from pandas import value_counts

from Card import Card
from itertools import combinations
from Hand import Hand
from Board import Board


def check(hand, board):
    set = hand.cards + board.cards
    set.sort(key=lambda x: x.getRank())
    combos = getAllPossibleCombinations(hand.cards, board.cards)
    combos = [list(combo) for combo in combos]
    NONE = 'Error'
    mapper = {
        'High Card': 1,
        'Pair': 2,
        'Two Pair': 3,
        'Three of a Kind': 4,
        'Straight': 5,
        'Flush': 6,
        'Full House': 7,
        'Four of a Kind': 8,
        'Straight Flush': 9,
        'Royal Flush': 10,
        NONE: 0
    }
    things = []
    for combo in combos:
        if royalFlush(combo):
            things.append('Royal Flush')
        elif straightFlush(combo):
            things.append('Straight Flush')
        elif fourOfAKind(combo):
            things.append('Four of a Kind')
        elif fullHouse(combo):
            things.append('Full House')
        elif flush(combo):
            things.append('Flush')
        elif straight(combo):
            things.append('Straight')
        elif threeOfAKind(combo):
            things.append('Three of a Kind')
        elif twoPair(combo):
            things.append('Two Pair')
        elif pair(combo):
            things.append('Pair')
        elif highCard(combo):
            things.append('High Card')
        else:
            things.append(NONE)
    strings = []
    for c in combos:
        l = []
        for card in c:
            l.append(str(card))
        strings.append(l)
    intermediate = pd.DataFrame({'combo': strings, 'thing': things})
    intermediate.to_csv('intermediate.csv')
    return max(things, key=lambda x: mapper[x])


# Auxiliary functions
def flush(set):
    series = pd.Series(set)
    suits = series.apply(lambda x: x.suit)
    return suits.value_counts().max() == 5

def straight(set):
    series = pd.Series(set)
    ranks = series.apply(lambda x: x.getRank())
    ranks = ranks.sort_values()
    expected = range(ranks.min(), ranks.max()+1)
    actual = sorted(ranks.to_list())
    diffs = ranks.diff()
    return list(expected) == actual and len(set) == 5

def pair(set):
    return getPairs(set) == 1

def twoPair(set):
    return getPairs(set) == 2
"""    series = pd.Series(set)
    ranks = series.apply(lambda x: x.getRank())
    return ranks.value_counts().max() == 2 and len(ranks.value_counts()) == 3"""

def threeOfAKind(set):
    series = pd.Series(set)
    ranks = series.apply(lambda x: x.getRank())
    return ranks.value_counts().max() == 3

def fourOfAKind(set):
    series = pd.Series(set)
    ranks = series.apply(lambda x: x.getRank())
    return ranks.value_counts().max() == 4

def fullHouse(set):
    series = pd.Series(set)
    ranks = series.apply(lambda x: x.getRank())
    return ranks.value_counts().max() == 3 and len(ranks.value_counts()) == 2 and len(set) == 5

def straightFlush(set):
    return straight(set) and flush(set)

def royalFlush(set):
    series = pd.Series(set)
    ranks = series.apply(lambda x: x.getRank()).to_list()
    return (sorted(ranks) == [10, 11, 12, 13, 14]) and flush(set)

def highCard(set):
    return True

def getAllPossibleCombinations(hand, board):
    c = []
    maxLen = len(hand) + len(board)
    for i in range(2, 6):
        c += list(combinations(hand + board, i))
    return c

def getPairs(set):
    series = pd.Series(set)
    ranks = series.apply(lambda x: x.getRank())
    valueCounts = ranks.value_counts()
    correct = valueCounts[valueCounts == 2].index
    return len(correct)


if __name__ == '__main__':
    hand = Hand()
    board = Board()
    hand.cards = [Card('10', 'Hearts'), Card('1', 'Diamonds')]
    board.cards = [
        Card('10', 'Clubs'), Card('10', 'Spades'), Card('3', 'Hearts'),
        Card('4', 'Hearts'), Card('5', 'Hearts')
    ]
    result = check(hand, board)
    print(result)