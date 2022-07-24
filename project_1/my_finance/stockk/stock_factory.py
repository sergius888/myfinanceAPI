import yfinance

# imports are done from the file which starts the app
from my_finance.exceptions import StockCodeInvalid
from my_finance.models import StockModel
from my_finance.stockk.stock import Stock


class StockFactory:
    # TODO what if we enter an invalid ticker?
    # TODO add yesterday's price & today's price, should update based on date
    def make_from_model(self, model: StockModel) -> Stock:
        try:
            yf_ticker = yfinance.Ticker(model.ticker)
            print(yf_ticker.info)
            company = yf_ticker.info["longName"]
            field = yf_ticker.info["sector"]
            long_summary = yf_ticker.info["longBusinessSummary"]
            exchange = yf_ticker.info["exchange"]
            country = yf_ticker.info["country"]
            number_of_employees = yf_ticker.info["fullTimeEmployees"]
            new_stock = Stock(model.ticker, company, field, country, number_of_employees)
            new_stock.set_long_summary(long_summary)
            new_stock.set_exchange(exchange)
            return new_stock
        except Exception:
            raise StockCodeInvalid()


#
#
#
# #
# yf_ticker = yfinance.Ticker("TSLA")
# price = yf_ticker.info["currentPrice"]
# prny = yf_ticker.info["previousClose"]
# print(price)
# print(prny)
# #
# #
# ce_y = yf_ticker.history(interval="1d", period="2d")
# print(ce_y["Close"])
# print(price_y["Close"])
#
# print("Pause")
# print(price_y["Close"].values[0])
# print(type(price_y))
#
#
# price_x = yf_ticker.history(interval="1d", period="5d")
# print(price_x["Close"])
#


# yf_ticker = yfinance.Ticker("MSFT")
#
# price_y = yf_ticker.history(interval="1d", period="2d")
#
# print(price_y["Close"])
# print(price_y["Close"].values[0])