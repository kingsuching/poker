from shiny import App, ui, render, reactive
from SuitsAndRanks import SUITS, RANKS
from analyzeHand import analyzeHand, check
from Card import Card
from Hand import Hand
from Board import Board

SIMULATIONS = 10
PLAYERS = 4

app_ui = ui.page_fluid(
    ui.panel_title("Poker Simulator"),

    ui.h3("Simulation Specifics"),
    ui.input_slider("n", "Number of Simulations", min=1, max=1000, value=SIMULATIONS),
    ui.input_slider("num_players", "Number of Players", min=2, max=10, value=PLAYERS),

    # User selects hand cards
    ui.h3("Select Hand"),
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
    ui.h3("Select Board"),
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
        ui.help_text("Need at least 3 cards."),
    ),

    ui.input_action_button("run_simulation", "Click for Probabilities"),
    ui.output_text_verbatim("result"),
)

def server(input, output, session):
    @reactive.Effect
    @reactive.event(input.run_simulation)
    def run_simulation():
        print('Run Simulation')
        try:
            rank1 = input.hand_rank1()
            suit1 = input.hand_suit1()
            rank2 = input.hand_rank2()
            suit2 = input.hand_suit2()
            card1 = Card(rank1, suit1)
            card2 = Card(rank2, suit2)
            hand_cards = [card1, card2]
            hand = Hand(deal_cards=False)
            hand.setCards(hand_cards)
        except ValueError:
            print('Could not set the cards in the hand')
            return

        # Parse the board cards
        board_cards = []
        for idx in range(1, 6):
            rank = getattr(input, f"board_rank{idx}")()
            suit = getattr(input, f"board_suit{idx}")()
            print(f'{rank} of {suit}')
            if rank is not None and suit is not None:
                try:
                    card = Card(rank, suit)
                except:
                    break
                board_cards.append(card)
        board = Board(True)
        board.setCards(board_cards)

        num_simulations = int(input.n())
        num_players = int(input.num_players())
        probabilities = analyzeHand(hand, board, n=num_simulations, players=num_players)
        print('analyzed it')
        guaranteed_hand = check(hand, board)
        text = f"\n\nGuaranteed Hand: {guaranteed_hand}"
        text += "\n\nProbabilities:"
        text += "\n" + str(probabilities)
        return text

if __name__ == '__main__':
    app = App(app_ui, server)
    app.run()