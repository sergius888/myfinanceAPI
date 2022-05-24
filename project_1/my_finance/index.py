# this is our root file, when we execute this we will start our app
# webpage for fastapi framework https://fastapi.tiangolo.com/tutorial/,
# also https://realpython.com/fastapi-python-web-apis/

# uvicorn index:app --reload --port 7777
# uvicorn is the server which will start
# index:app, index -> the file name, app -> the FastAPI object name
# --reload -> the server will restart when we modify the codepy
# --port <port_number> -> select on which port to start

import yfinance
import logging
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi_utils.tasks import repeat_every

from my_finance.stockk.stock_repo import StockRepository
from my_finance.configuration.config import Configuration
from my_finance.database.stock_file_persistance import StockFilePersistance
from my_finance.database.stock_sql_persistance import StockSqlPersistance
from my_finance.exceptions import StockNotFound, StockAlreadyAdded
from my_finance.api.stocks import stocks_router
from my_finance.api.health import health_router
from my_finance.api.diagrams import diagrams_router

app = FastAPI(
    title="MyFinance API",
    # <major_version>.<minor_version>.<patch_version>
    version="1.0.0",  # increase version after finishing homework
    description="A web application that allows you to access financial data, "
    "stock prices and charts, using Yahoo Finance data",
)
app.include_router(stocks_router)
app.include_router(health_router)
app.include_router(diagrams_router)

conf = Configuration()
if conf.get_db_type() == "file":
    persistance = StockFilePersistance(conf.get_db_path())
if conf.get_db_type() == "sql":
    persistance = StockSqlPersistance(conf.get_db_path())
StockRepository.persistance = persistance
stock_repo = StockRepository()

logging.basicConfig(filename="finance.log", encoding="utf-8", level=logging.DEBUG)
logging.info("Starting the finance app ...")



@app.on_event("startup")
def load_list_of_items():
    logging.info("Loading stocks from database ...")
    stock_repo.load()
    logging.info("Successfully loaded stocks from database.")


@app.on_event("startup")
@repeat_every(seconds=5 * 60, wait_first=True)  # every 5 seconds we run this function
def update_prices():
    # get all stocks
    # get price (yfinance)
    # stockk set price
    if not stock_repo.stocks:
        logging.warning("Stocks not loaded yet!")
        return
    tickers = stock_repo.stocks.keys()
    logging.info("Updating prices ...")
    for a_ticker in tickers:
        yf_ticker = yfinance.Ticker(a_ticker)
        price = yf_ticker.info["currentPrice"]
        stock_repo.stocks[a_ticker].set_price(price)


@app.exception_handler(StockNotFound)
def handle_stock_not_found(exception, request):
    return JSONResponse(
        content="The stock you requested was not saved in our app!", status_code=404
    )


@app.exception_handler(StockAlreadyAdded)
def stock_already_added(exception, request):
    return JSONResponse(
        content="The stock is already added in our app.", status_code=400
    )
