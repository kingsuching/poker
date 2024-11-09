from shiny import App, ui, render, reactive
from SuitsAndRanks import SUITS, RANKS
from analyzeHand import analyzeHand, check
from Card import Card
from Hand import Hand
from Board import Board
from numbersValues import *;

app_ui = ui.page_fluid(
    ui.panel_title("Poker Simulator"),
    ui.h3("Simulation Specifics"),
    ui.input_slider("n", "Number of Simulations", min=MIN_SIMULATIONS, max=MAX_SIMULATIONS, value=SIMULATIONS),
    ui.input_slider("num_players", "Number of Players", min=MIN_PLAYERS, max=MAX_PLAYERS, value=PLAYERS),

    # User selects hand cards
    ui.h3("Hand"),
    ui.panel_well(
        ui.row(
            ui.column(
                6,
                ui.input_select("hand_rank1", "Hand Card 1 Rank", RANKS),
                ui.input_select("hand_suit1", "Hand Card 1 Suit", SUITS),
            ),
            ui.column(
                6,
                ui.input_select("hand_rank2", "Hand Card 2 Rank", RANKS),
                ui.input_select("hand_suit2", "Hand Card 2 Suit", SUITS),
            ),
        ),
    ),

    # User selects board cards
    ui.h3("Board"),
    ui.panel_well(
        ui.row(
            *[
                ui.column(
                    2,
                    ui.input_select(f"board_rank{i}", f"Board Card {i} Rank", [""] + RANKS),
                    ui.input_select(f"board_suit{i}", f"Board Card {i} Suit", [""] + SUITS),
                )
                for i in range(1, 6)
            ]
        ),
        ui.help_text("Need at least 3 cards.\n"),
        ui.help_text('Note: all probabilities based off the river.')
    ),

    ui.input_action_button("run_simulation", "Click for Probabilities"),
    ui.output_text_verbatim("result"),
)

def server(input, output, session):
    resultText = reactive.Value("")

    @reactive.Effect
    @reactive.event(input.run_simulation)
    def run_simulation():
        print('Run Simulation')
        # Parse hand cards
        try:
            rank1 = input.hand_rank1()
            suit1 = input.hand_suit1()
            rank2 = input.hand_rank2()
            suit2 = input.hand_suit2()
            card1 = Card(rank1, suit1)
            card2 = Card(rank2, suit2)
            hand_cards = [card1, card2]
            hand = Hand(False)
            hand.setCards(hand_cards)
        except ValueError as e:
            resultText.set(f"Error in hand card selection: {e}")
            return

        # Parse the board cards
        board_cards = []
        for idx in range(1, 6):
            rank = getattr(input, f"board_rank{idx}")()
            suit = getattr(input, f"board_suit{idx}")()
            if rank and suit:
                try:
                    card = Card(rank, suit)
                except ValueError as e:
                    resultText.set(f"Error in board card {idx} selection: {e}")
                    return
                board_cards.append(card)

        board = Board(False)
        board.setCards(board_cards)

        num_simulations = int(input.n())
        num_players = int(input.num_players())
        probabilities = analyzeHand(hand, board, n=num_simulations, players=num_players)
        guaranteed = check(hand, board)
        text = f"\n\nYou have a {guaranteed}"
        text += "\n\n"
        for key in probabilities.index:
            value = probabilities[key]*100
            text += f'{key}: {value}%\n'
        resultText.set(text)

    @output
    @render.text
    def result():
        return resultText.get()

if __name__ == '__main__':
    app = App(app_ui, server)
    app.run()