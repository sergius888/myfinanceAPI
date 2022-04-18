import yfinance

# imports are done from the file which starts the app
from models import FutureModel
from derivatives.future import Future

class FutureFactory:

    def make_from_model(self, model: FutureModel) -> Future:
        yf_ticker = yfinance.Ticker(model.ticker)
        print(yf_ticker.info)
        name = yf_ticker.info["shortName"]
        exchange = yf_ticker.info["exchange"]
        current_price = yf_ticker.info["previousClose"]
        lowest_52 = yf_ticker.info["fiftyTwoWeekLow"]
        highest_52 = yf_ticker.info["fiftyTwoWeekHigh"]
        new_future = Future(model.ticker, name, current_price, lowest_52, highest_52)
        new_future.set_exchange(exchange)
        return new_future