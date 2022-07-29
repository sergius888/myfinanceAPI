class Stock:
    def __init__(
        self,
        ticker: str,
        company_name: str,
        field: str,
        country: str,
        number_of_employees: int,
        amount: float = 0,
        shares_cost: float = 0,
        profit_and_loss: float = 0,
        transactions=None
    ):
        if transactions is None:
            transactions = []
        self.ticker = ticker
        self.company = company_name
        self.field = field
        self.amount = amount
        self.long_summary = ""
        self.exchange = ""
        self.country = country
        self.number_of_employees = number_of_employees
        self.price = -1
        self.shares_cost = shares_cost
        self.profit_and_loss = profit_and_loss
        self.transactions = transactions


    def set_long_summary(self, summary: str):
        self.long_summary = summary

    def set_exchange(self, exchange: str):
        self.exchange = exchange

    def set_price(self, value: float):
        print(value)
        self.price = value

    def set_p_and_l(self):
        self.profit_and_loss = self.price - self.shares_cost
        print(self.profit_and_loss)



