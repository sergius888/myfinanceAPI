from flask import Flask, render_template
from my_finance.stock.stock_repo import StockRepository
from my_finance.configuration.config import Configuration
from my_finance.database.stock_file_persistance import StockFilePersistance
from my_finance.database.stock_sql_persistance import StockSqlPersistance

app = Flask(__name__)

conf = Configuration()
print(conf.get_db_type())
if conf.get_db_type() == "file":
    print('file x 2')
    persistance = StockFilePersistance(conf.get_db_path())
if conf.get_db_type() == "sql":
    persistance = StockSqlPersistance(conf.get_db_path())
StockRepository.persistance = persistance
stock_repo = StockRepository()
stock_repo.load()


@app.route("/")
def hello():
    stocks = stock_repo.get_all()
    print(stocks)
    return render_template("stocks.html", stocks=stocks)