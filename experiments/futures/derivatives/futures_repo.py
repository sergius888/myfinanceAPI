from derivatives.future import Future
from exceptions import FutureNotFound


class FuturesRepository:
    futures = {}
    persistance = None

    @staticmethod
    def add(new_future: Future):
        FuturesRepository.futures[new_future.ticker] = new_future
        future_info = {
            "symbol": new_future.symbol,
            "shortName": new_future.name,
            "exchange": new_future.exchange,
            "previousClose": new_future.current_price,
            "fiftyTwoWeekHigh": new_future.highest_52,
            "fiftyTwoWeekLow": new_future.lowest_52,
            # "yesterday_price": new_future.number_of_employees,
        }
        FuturesRepository.persistance.add(future_info)

    @staticmethod
    def get_all_contracts() -> list[Future]:
        print([f.price for f in FuturesRepository.futures.values()])
        return list(FuturesRepository.futures.values())

    # if we do not have the future, we can raise an error or return None
    @staticmethod
    def get_by_symbol(symbol: str) -> Future:
        if symbol in FuturesRepository.futures.keys():
            return FuturesRepository.futures[symbol]
        else:
            raise FutureNotFound()
        # return StockFactory().make_extended_stock(ticker)

    @staticmethod
    def remove(future_id: str):
        FuturesRepository.futures.pop(future_id)
        FuturesRepository.persistance.remove(future_id)

    @staticmethod
    def load():
        items = FuturesRepository.persistance.get_all()
        # items = list of dictionaries from the file
        for one_item in items:
            new_future = Future(one_item["ticker"], one_item["shortName"], one_item["previousClose"],
                              one_item["fiftyTwoWeekHigh"], one_item["fiftyTwoWeekLow"])
            if "exchange" in one_item:
                new_future.set_exchange(one_item["exchange"])
            FuturesRepository.futures[one_item["ticker"]] = new_future
