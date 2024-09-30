from Constants import global_deck


class Board:
    def __init__(self):
        self.deck = global_deck
        self.cards = []

    def flop(self):
        if len(self.cards) == 0:
            self.deck.draw()
            self.cards = [self.deck.draw(), self.deck.draw(), self.deck.draw()]
            return True
        else:
            print("Flop already dealt")
            return False

    def turn(self):
        if len(self.cards) == 3:
            self.deck.draw()
            self.cards.append(self.deck.draw())
            return True
        elif len(self.cards) == 4:
            print("Turn already dealt")
            return False
        else:
            print("Flop not dealt")
            return False

    def river(self):
        if len(self.cards) == 4:
            self.deck.draw()
            self.cards.append(self.deck.draw())
            return True
        elif len(self.cards) == 5:
            print("River already dealt")
            return False
        elif len(self.cards) < 4:
            print("Flop not dealt")
            return False

    def setCards(self, cards):
        self.cards = cards
        for card in cards:
            try:
                self.deck.cards.remove(card)
            except:
                print(f'{card} not in deck')
                pass

    def __copy__(self):
        b = Board()
        b.cards = self.cards.copy()
        b.deck = self.deck
        return b