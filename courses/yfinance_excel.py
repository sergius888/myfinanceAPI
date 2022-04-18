import yfinance
import openpyxl

ticker = yfinance.Ticker("PFE")
history = ticker.history("3y")

history.to_excel("yfinance.xlsx")
