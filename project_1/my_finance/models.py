from pydantic import BaseModel, Field


# if another domain in your project, create different models for POST & GET
class StockModel(BaseModel):
    ticker: str = Field(
        description="The ticker ID of the stock, for example Tesla has TSLA"
    )
    company: str = Field(
        default="", description="The full company name, leave empty for POST"
    )
    field: str = Field(default="")
    price: float = Field(default=-1, description="Current price updated in real time")
    amount: float = Field(default=0, description="The amount of shares you own")
    shares_cost: float = Field(default=0, description="The value of the shares you own")
    profit_loss: float = Field(default=0, description="Current p/l updated in real time")
    transactions: list = Field(default=[], description="List of transactions with datetime.")

    class Config:
        orm_mode = True


class StockExtendedModel(StockModel):
    long_summary: str = Field(description="The business summary of the company")
    exchange: str = Field(
        description="The name of the exchange where the company is listed"
    )
    country: str = Field(description="The country of company's headquarter")
    number_of_employees: str = Field(description="Number of employees")



class DiagramModel(BaseModel):
    tickers: list[str] = Field()
    info: str = Field(default="Close", description="Values: Open, Close, High, Low")
    start_date: str = Field(default="2015-06-01", description="Format: YYYY-MM-DD")
    end_date: str = Field(default=None)
