from collections import Counter

from Board import Board
from Deck import Deck
from Player import Player
from PokerHandCheck import *
from tqdm import tqdm

if __name__ == '__main__':
    N = 100
    NUM_PLAYERS = 5
    players = [Player(name=f"Player {i+1}") for i in range(NUM_PLAYERS)]
    hand_types = []
    flop_hand_types = []
    turn_hand_types = []
    dealer_position = -1

    for i in tqdm(range(N)):
        global_deck = Deck()
        dealer_position = (dealer_position + 1) % NUM_PLAYERS
        for player in players:
            player_index = (dealer_position + 1 + players.index(player)) % NUM_PLAYERS
            player.hand = Hand()
        board = Board()
        board.flop()
        board.turn()
        board.river()
        best_flop_hand = None
        best_turn_hand = None
        best_river_hand = None
        for player in players:
            flop_board = Board()
            turn_board = Board()
            flop_board.cards = board.cards[:3]
            turn_board.cards = board.cards[:4]
            fht = check(player.hand, flop_board)
            tht = check(player.hand, turn_board)
            rht = check(player.hand, board)
            if best_flop_hand is None or fht > best_flop_hand:
                best_flop_hand = fht
            if best_turn_hand is None or tht > best_turn_hand:
                best_turn_hand = tht
            if best_river_hand is None or rht > best_river_hand:
                best_river_hand = rht
        hand_types.append(best_river_hand)
        flop_hand_types.append(best_flop_hand)
        turn_hand_types.append(best_turn_hand)
    flopSeries = pd.Series(flop_hand_types)
    turnSeries = pd.Series(turn_hand_types)
    riverSeries = pd.Series(hand_types)
    assert len(flopSeries) == N and len(turnSeries) == N and len(riverSeries) == N
    print("Flop Winning Hand Types:")
    print(flopSeries.value_counts(normalize=True))
    print("\nTurn Winning Hand Types:")
    print(turnSeries.value_counts(normalize=True))
    print("\nRiver Winning Hand Types:")
    print(riverSeries.value_counts(normalize=True))
