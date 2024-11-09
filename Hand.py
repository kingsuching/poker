import Deck
from Constants import global_deck
import pandas as pd
import numpy as np

class Hand:
    def __init__(self, deal_cards=True):
        self.deck = global_deck
        if deal_cards:
            self.cards = [self.deck.draw(), self.deck.draw()]
        else:
            self.cards = []

    def __str__(self):
        return ' '.join(str(card) for card in self.cards)

    def setCards(self, cards):
        self.cards = cards
        for card in cards:
            try:
                self.deck.cards.remove(card)
            except:
                print(f'{card} not in deck')
                pass

    def __eq__(self, other):
        return self.cards == other.cards

    def __gt__(self, other):
        df = pd.DataFrame()
        df.append(self.cards)
        df.append(other.cards)
        df['Which'] = ['self', 'self', 'other', 'other']
        df['Suit'] = df[0].apply(lambda c: c.suit)
        df['Rank'] = df[0].apply(lambda c: c.getRank())
        maxIndex = df['Rank'].max()
        return maxIndex['Which'] == 'self'

    def __lt__(self, other):
        return (not self == other) and not self > other