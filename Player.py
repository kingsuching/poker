from Hand import Hand

class Player:
    def __init__(self, name, stack=10.00, cpu=False):
        self.name = name
        self.stack = stack
        self.hand = Hand(False)
        self.folded = False
        self.all_in = False
        self.bet = 0
        self.cpu = cpu

    def bet(self, amount):
        if self.folded or self.all_in:
            return 0.0
        self.stack -= amount
        self.bet += amount
        return amount

    def fold(self):
        self.folded = True
