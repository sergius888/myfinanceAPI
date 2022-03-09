# this is our root file, when we execute this we will start our app
# webpage for fastapi framework https://fastapi.tiangolo.com/tutorial/,
# also https://realpython.com/fastapi-python-web-apis/

# uvicorn index:app --reload --port 7777
# uvicorn is the server which will start
# index:app, index -> the file name, app -> the FastAPI object name
# --reload -> the server will restart when we modify the code
# --port <port_number> -> select on which port to start


from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi_utils.tasks import repeat_every

from stock.stock_repo import StockRepository
from configuration.config import Configuration
from database.stock_file_persistance import StockFilePersistance
from database.stock_sql_persistance import StockSqlPersistance
from exceptions import StockNotFound
from api.stocks import stocks_router
from api.health import health_router

app = FastAPI(
    title="Name of our app",  # TODO for homework, name your application
    # <major_version>.<minor_version>.<patch_version>
    version="0.2.0",  # increase version after finishing homework
    description="",  # TODO add a description
)
app.include_router(stocks_router)
app.include_router(health_router)

conf = Configuration()
if conf.get_db_type() == "file":
    persistance = StockFilePersistance(conf.get_db_path())
if conf.get_db_type() == "sql":
    persistance = StockSqlPersistance(conf.get_db_path())
StockRepository.persistance = persistance
stock_repo = StockRepository()


import logging
logging.basicConfig(filename="finance.log", encoding="utf-8", level=logging.DEBUG)
logging.info("Starting the finance app ...")

# TODO create a get for a single stock, we give the ticker and receive more information
# additional information: long summary, on which exchange it is, country, number of employees, industry


@app.on_event("startup")
def load_list_of_items():
    logging.info("Loading stocks from database ...")
    stock_repo.load()
    logging.info("Successfully loaded stocks from database ...")

import yfinance

@app.on_event("startup")
@repeat_every(seconds=5 * 60, wait_first=True)
def update_prices():
    # get all stocks
    # get price (yfinance)
    # stock set price
    if not stock_repo.stocks:
        logging.warning("Stocks not loaded yet!")
        return
    # print("ssss ------ sssss")
    tickers = stock_repo.stocks.keys()
    logging.info("Updating prices ...")
    for a_ticker in tickers:
        yf_ticker = yfinance.Ticker(a_ticker)
        price = yf_ticker.info["currentPrice"]
        stock_repo.stocks[a_ticker].set_price(price)


@app.exception_handler(StockNotFound)
def handle_stock_not_found(exception, request):
    return JSONResponse(content="The stock you requested was not saved in our app!", status_code=404)