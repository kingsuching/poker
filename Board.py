import Deck
import Card
import random
from Constants import global_deck


class Board:
    def __init__(self):
        self.deck = global_deck
        self.cards = []

    def flop(self):
        if len(self.cards) == 0:
            self.deck.draw()
            self.cards = [self.deck.draw(), self.deck.draw(), self.deck.draw()]
        else:
            print("Flop already dealt")

    def turn(self):
        if len(self.cards) == 3:
            self.deck.draw()
            self.cards.append(self.deck.draw())
        elif len(self.cards) == 4:
            print("Turn already dealt")
        else:
            print("Flop not dealt")

    def river(self):
        if len(self.cards) == 4:
            self.deck.draw()
            self.cards.append(self.deck.draw())
        elif len(self.cards) == 5:
            print("River already dealt")
        elif len(self.cards) < 4:
            print("Flop not dealt")