from my_finance.stockk.stock import Stock
from my_finance.exceptions import StockNotFound, CannotAddStock, StockAlreadyAdded


class StockRepository:
    stocks = {}
    persistence = None



    @staticmethod
    def add(new_stock: Stock):
        stock_info = {
            "ticker": new_stock.ticker,
            "company": new_stock.company,
            "amount": new_stock.amount,
            "field": new_stock.field,
            "longSummary": new_stock.long_summary,
            "exchange": new_stock.exchange,
            "country": new_stock.country,
            "numberOfEmployees": new_stock.number_of_employees,
        }
        if new_stock.ticker not in StockRepository.stocks:
            try:
                StockRepository.persistence.add(stock_info)
            except Exception as e:
                raise CannotAddStock("Could not add stock. Reason: " + str(e))
            StockRepository.stocks[new_stock.ticker] = new_stock
        else:
            raise StockAlreadyAdded()

    @staticmethod
    def get_all() -> list[Stock]:
        print([s.price for s in StockRepository.stocks.values()])
        return list(StockRepository.stocks.values())

    # if we do not have the stock, we can raise an error or return None
    @staticmethod
    def get_by_ticker(ticker: str) -> Stock:
        if ticker in StockRepository.stocks.keys():
            return StockRepository.stocks[ticker]
        else:
            raise StockNotFound()
        # return StockFactory().make_extended_stock(ticker)



    @staticmethod
    def remove(stock_id: str):
        if stock_id in StockRepository.stocks.keys():
            StockRepository.stocks.pop(stock_id)
            StockRepository.persistence.remove(stock_id)
        else:
            raise StockNotFound()


    @staticmethod
    def load():
        items = StockRepository.persistence.get_all()
        # items = list of dictionaries from the file
        for one_item in items:
            new_stock = Stock(
                one_item["ticker"],
                one_item["company"],
                one_item["field"],
                one_item["country"],
                one_item["numberOfEmployees"],
                one_item["amount"],
            )
            if "longSummary" in one_item and "exchange" in one_item:
                new_stock.set_long_summary(one_item["longSummary"])
                new_stock.set_exchange(one_item["exchange"])
            StockRepository.stocks[one_item["ticker"]] = new_stock


    @staticmethod
    def edit_amount(ticker_id: str, amnt: float):
        if ticker_id in StockRepository.stocks.keys():
            StockRepository.persistence.update(ticker_id, amnt)
        else:
            raise StockNotFound()




