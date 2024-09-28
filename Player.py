import pandas as pd
import numpy as np

from Card import Card
from itertools import combinations
from Hand import Hand
from Board import Board

class Player:
    def __init__(self, name, stack=10.00, cpu=False):
        self.name = name
        self.stack = stack
        self.hand = Hand()
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
