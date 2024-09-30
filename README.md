# poker

## Game Simulation

Run simulation of poker games and analyze the results.

Default simulation is **100** games with **5** players.

`python simulate.py`

`python simulate.py <_games_> <_players_>`

---------

## Outcome Probability

To run the simulation with a hand and board, use the following command:

`python analyzeHand.py`

The default behavior is to read the cards from a file called `handAndBoard.xlsx`, with the hand and board being in the respective sheets.

However, one can use user input if desired in the following format line-by-line:

<rank>9 </rank> of <suit>Spades</suit>

Lastly, one can also modify the contents of `handAndBoard.txt` to change the hand and board using the same formatting.