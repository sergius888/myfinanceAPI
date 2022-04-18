# add a new router for futures (oil, oats, etc)
 # examples of tickers: for oil -> CL=F, for wheat -> ZW=F
 # create a new object to represent the data from futures
 #       -> name, exchange, symbol, lowest price in 52weeks, highest price in 52weeks, yesterday price, current price
 # create a repo for it and a new table in our database
 # current price should be refreshed every 10min, other pirces once per day
 # add at least 2 futures & have a get to list all of them with their data

#
# from fastapi import APIRouter
#
# futures_router = APIRouter(prefix="/futures")
#
#
#
# @futures_router.post("")


import yfinance as yf

from courses.project_1.my_finance.models import FutureModel
from experiments.futures.derivatives.future import Future

# oil = yf.Ticker("CL=F")

#
# print(oil.info["symbol"])
# print(oil.info['fiftyTwoWeekHigh'])
# print(oil.info['previousClose'])

# oil.history(period="2d")
#
#
# oil.history(period="1d")


# def make_from_model(model: StockModel) -> Stock:
#     yf_ticker = yf.Ticker(model.ticker)
#     print(yf_ticker)
#
# make_from_model(oil)


def make_model(model: FutureModel) -> Future:
    yf_ticker = yf.Ticker(model.symbol)
    print(yf_ticker)

make_model("CL=F")