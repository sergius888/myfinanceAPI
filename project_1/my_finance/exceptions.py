

class StockNotFound(Exception):
    # it handles both requests,
    # get stock that doesn't exist and delete stock that doesn't exist.
    pass


class CannotAddStock(Exception):
    pass


class StockAlreadyAdded(Exception):
    pass


