from pydantic import BaseModel, Field


# TODO create model for adding a stock & a model for getting a stock
# if another domain in your project, create different models for POST & GET
class StockModel(BaseModel):
    ticker: str = Field(description="The ticker ID of the stock, for example Tesla has TSLA")
    company: str = Field(default="", description="The full company name, leave empty for POST")
    field: str = Field(default="")
    price: float = Field(default=-1, description="Current price updated in real time")

    class Config:
        orm_mode = True


class StockExtendedModel(StockModel):
    long_summary: str = Field(description="The business summary of the company")
    exchange: str = Field(description="The name of the exchange where the company is listed")
    country: str = Field()  # TODO add description
    number_of_employees: str = Field()  # TODO add description

class FutureModel(BaseModel):
    name: str = Field(description="The name of the future contract")
    ticker: str = Field(description="The ticker symbol of the future contract, for example oil has CL=F")
    exchange: str = Field(description="The name of the exchange where the company is listed")
    current_price: float = Field(default=-1, description="Current price updated in real time")
    lowest_52: str = Field(default=-1, description="Lowest price in 52 weeks")
    highest_52: str = Field(default=-1, description="Highest price in 52 weeks")


class DiagramModel(BaseModel):
    tickers: list[str] = Field()
    info: str = Field(default="Close", description="Values: Open, Close, High, Low")
    start_date: str = Field(default="2015-06-01", description="Format: YYYY-MM-DD")
    end_date: str = Field(default=None)