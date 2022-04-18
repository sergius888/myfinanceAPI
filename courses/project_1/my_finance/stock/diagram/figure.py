import yfinance
from plotly import graph_objects
# from matplotlib import pyplot


from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


import random

from courses.project_1.my_finance.models import DiagramModel


def show_simple_diagram(ticker_id: str, info: str = "Close", interval: str = "3y"):
    dataframe = __get_the_data_frame(interval, ticker_id)
    # draw the plot/figure/diagram
    scatter = graph_objects.Scatter(x=dataframe.index, y=dataframe[info])
    diagram = graph_objects.Figure([scatter])
    diagram.show()


def create_and_save_to_file(model: DiagramModel):
    dataframe = yfinance.download(model.tickers, start=model.start_date, end=model.end_date)
    figure, axis = plt.subplots(figsize=(16, 9))
    for key in dataframe[model.info]:
        axis.plot(dataframe[model.info].index, dataframe[model.info][key])
    plt.title(f"{'-'.join(model.tickers)} stock price evolution")
    plt.xlabel("Date")
    plt.ylabel("Price")
    axis.legend(dataframe[model.info].columns.values)
    plt.savefig(f"./stock/diagram/diagram_nr_{random.randrange(1000, 9999)}")


def __get_the_data_frame(interval, ticker_id):
    tsla = yfinance.Ticker(ticker_id)
    dataframe = tsla.history(interval)
    dataframe.reset_index()
    return dataframe
