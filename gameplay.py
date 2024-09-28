import pandas as pd
import numpy as np

from Card import Card
from itertools import combinations

from Deck import Deck
from Hand import Hand
from Board import Board
from Player import Player


class Game:
    def __init__(self, n_players=4, blind=0.10):
        self.board = Board()
        self.hand = Hand()
        self.deck = self.board.deck
        self.n_players = n_players
        self.small_blind = blind
        self.big_blind = 2 * blind
        self.pot = 0
        self.players = []
        self.rounds = 0
        self.players = [Player('Yourself')]
        for i in range(2, n_players+1):
            self.players.append(Player('CPU ' + str(i), cpu=True))
        self.current_player = 0
        self.dealer = 0
        self.big_blind_player = 1
        self.small_blind_player = 2
        self.deck = []


    def deal(self):
        # Write a function that deals two cards to each player
        for player in self.players:
            player.hand = Hand()
            player.hand.cards = [self.deck.draw(), self.deck.draw()]
        self.rounds += 1

    def flop(self):
        # Write a function that deals the flop
        self.board.flop()
        self.rounds += 1

    def turn(self):
        # Write a function that deals the turn
        self.board.turn()
        self.rounds += 1

    def river(self):
        # Write a function that deals the river
        self.board.river()
        self.rounds += 1

    def bet(self, amount):
        # Write a function that allows the current player to bet
        self.pot += self.players[self.current_player].bet(amount)
        self.current_player += 1
        self.current_player %= self.n_players