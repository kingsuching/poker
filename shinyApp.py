from shiny import App, ui, render
from SuitsAndRanks import SUITS, RANKS

app_ui = ui.page_fluid(
    ui.panel_title("Poker Simulator"),
    ui.input_slider("n", "N", 0, 100, 1),
    ui.output_text_verbatim("txt"),
)

def server(input, output, session):
    @render.text
    def txt():
        return f'n squared = {input.n()**2}'

app = App(app_ui, server)

if __name__ == '__main__':
    app.run()