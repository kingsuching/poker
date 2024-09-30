import random
from Card import Card
from SuitsAndRanks import SUITS, RANKS

random.seed(42)


class Deck:
    def __init__(self, onBoard=False):
        self.cards = []
        self.suits = SUITS
        self.ranks = RANKS
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
