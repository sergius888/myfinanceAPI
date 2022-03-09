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