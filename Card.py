from SuitsAndRanks import SUITS, RANKS

class Card:
    def __init__(self, rank, suit, onBoard=False):
        self.rank = rank
        self.suit = suit
        self.onBoard = onBoard
        if self.rank not in RANKS or self.suit not in SUITS:
            raise ValueError(f"Invalid card: {self}")

    def __str__(self):
        return f"{self.rank} {self.suit}"

    def __gt__(self, other):
        if self.suit == other.suit:
            return self.getRank() > other.getRank()
        return self.suit > other.suit

    def __lt__(self, other):
        if self.suit == other.suit:
            return self.getRank() < other.getRank()
        return self.suit < other.suit

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def getRank(self):
        try:
            return int(self.rank)
        except:
            if self.rank == 'J':
                return 11
            elif self.rank == 'Q':
                return 12
            elif self.rank == 'K':
                return 13
            elif self.rank == 'A':
                return 14
            raise ValueError(f"Invalid rank: {self.rank}")