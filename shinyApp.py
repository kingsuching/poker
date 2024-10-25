from shiny import App, ui, render

app_ui = ui.page_fluid(
    ui.input_slider("n", "Sample Size", 0, 1000, 20),
    ui.output_plot("dist")
)

def server(input, output, session):
    @render.plot
    def dist():
        import numpy as np
        import matplotlib.pyplot as plt
        x = np.random.randn(input.n())
        plt.hist(x)

app = App(app_ui, server)

if __name__ == '__main__':
    app.run()