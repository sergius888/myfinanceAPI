# add a new router for futures (oil, oats, etc)
# examples of tickers: for oil -> CL=F, for wheat -> ZW=F
# create a new object to represent the data from futures
#       -> name, exchange, symbol, lowest price in 52weeks, highest price in 52weeks, yesterday price, current price
# create a repo for it and a new table in our database
# current price should be refreshed every 10min, other pirces once per day
# add at least 2 futures & have a get to list all of them with their data


class Future:
    def __init__(self, name: str, ticker: str):
        self.name = name
        self.symbol = ticker
        self.exchange = ""
        self.current_price = -1
        self.yesterday_price = -1
        self.lowest_52 = -1
        self.highest_52 = -1

    def set_exchange(self, exchange: str):
        self.exchange = exchange

    def set_current_price(self, current_price: float):
        self.current_price = current_price

    def set_yesterday_price(self, yesterday_price: float):
        self.yesterday_price = yesterday_price

    def set_lowest_52(self, lowest_52: float):
        self.lowest_52 = lowest_52

    def set_highest_52(self, highest_52: float):
        self.highest_52 = highest_52
