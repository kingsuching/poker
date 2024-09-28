from Card import Card
import random

class Deck:
    def __init__(self, onBoard=False):
        self.cards = []
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        for suit in self.suits:
            for rank in self.ranks:
                card = Card(rank, suit, onBoard)
                self.cards.append(card)
        assert len(self.cards) == 52
        self.discard = []
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if len(self.cards) == 0:
            self.cards = self.discard
            self.discard = []
            assert len(self.cards) != 0
            self.shuffle()
            # print("Reshuffled")
        card = self.cards.pop()
        self.discard.append(card)
        return card

    def __len__(self):
        return len(self.cards)
