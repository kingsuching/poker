import Deck
from Constants import global_deck

class Hand:
    def __init__(self, deal_cards=True):
        self.deck = global_deck
        if deal_cards:
            self.cards = [self.deck.draw(), self.deck.draw()]
        else:
            self.cards = []

    def __str__(self):
        return ' '.join(str(card) for card in self.cards)