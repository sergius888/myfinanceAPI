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
import webbrowser
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi_utils.tasks import repeat_every

import my_finance.stockk.stock_repo
from my_finance.stockk.stock_repo import StockRepository
from my_finance.configuration.config import Configuration
from my_finance.database.stock_file_persistence import StockFilePersistance
from my_finance.database.stock_sql_persistence import StockSqlPersistance
from my_finance.exceptions import StockNotFound, StockAlreadyAdded, StockCodeInvalid
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
    persistence = StockFilePersistance(conf.get_db_path())
if conf.get_db_type() == "sql":
    persistence = StockSqlPersistance(conf.get_db_path())
StockRepository.persistence = persistence
stock_repo = StockRepository()

logging.basicConfig(filename="finance.log", encoding="utf-8", level=logging.DEBUG)
logging.info("Starting the finance app ...")



@app.on_event("startup")
def load_list_of_items():
    logging.info("Loading stocks from database ...")
    print("FIRST LOGG INFO")
    stock_repo.load()
    print("FIRST LOAD INFO")
    logging.info("Successfully loaded stocks from database.")
    print("Last log event")
    # if stock_repo.stocks:
    #     tickers = stock_repo.stocks.keys()
    #     logging.info("Potential P/L updating in database ...")
    #     for a_ticker in tickers:
    #         print(f'Updating P/L for {a_ticker}')
    #         yf_ticker = yfinance.Ticker(a_ticker)
    #         price = yf_ticker.info["currentPrice"]
    #         price = round(price, 2)
    #         time = my_finance.stockk.stock_repo.date_string
    #         persistence.update_profit_loss(a_ticker, price, time)

@app.on_event("startup")
@repeat_every(seconds=5 * 30, wait_first=True)  # every 5 seconds we run this function
def update_prices():
    # get all stocks
    # get price (yfinance)
    # stock set price
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
    # raised for get and delete stocks which does not exist.
    return JSONResponse(
        content="The stock you requested was not saved in our app!", status_code=404
    )


@app.exception_handler(StockAlreadyAdded)
def stock_already_added(exception, request):
    return JSONResponse(
        content="The stock is already added in our app.", status_code=400
    )

@app.exception_handler(StockCodeInvalid)
def stock_already_added(exception, request):
    return JSONResponse(
        content="The stock code requested is not valid. Please check again!", status_code=500
    )





# def get_current_price(symbol):
#     ticker = yfinance.Ticker(symbol)
#     todays_data = ticker.history(period='1d')
#     return todays_data['Close'][0]
#
# print(get_current_price('TSLA'))



