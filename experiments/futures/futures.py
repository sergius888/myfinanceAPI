# add a new router for futures (oil, oats, etc)
 # examples of tickers: for oil -> CL=F, for wheat -> ZW=F
 # create a new object to represent the data from futures
 #       -> name, exchange, symbol, lowest price in 52weeks, highest price in 52weeks, yesterday price, current price
 # create a repo for it and a new table in our database
 # current price should be refreshed every 10min, other pirces once per day
 # add at least 2 futures & have a get to list all of them with their data

from fastapi import APIRouter

from models import FutureModel
from derivatives.future_factory import FutureFactory
from derivatives.futures_repo import FuturesRepository

futures_router = APIRouter(prefix="/futures")
futures_repo = FuturesRepository()


@futures_router.post("")
def add_new_future(future_info: FutureModel):
    new_future = FutureFactory().make_from_model(future_info)
    futures_repo.add(new_future)


@futures_router.get("", response_model=list[FutureModel])
def get_stocks(field: str = None, page: int = None, items_per_page: int = None):
    futures = futures_repo.get_all_contracts()
    if field:
        futures = [f for f in futures if f.field == field]
    if page is not None and page >= 0:
        # below, it's called a ternary operator
        number_of_items_per_page = items_per_page if items_per_page else conf.get_number_of_items_per_page()
        # page = 0, 0:2
        # page = 1, 2:4
        futures = futures[page * number_of_items_per_page:(page + 1) * number_of_items_per_page]
    return futures


@futures_router.get("/{ticker_id}", response_model=FutureModel)
def get_one_stock(ticker_id: str):
    return futures_repo.get_by_symbol(ticker_id)


