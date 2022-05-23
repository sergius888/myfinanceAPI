from flask import Flask, render_template, redirect, url_for, request
from my_finance.stockk.stock_repo import StockRepository
from my_finance.stockk.stock_factory import StockFactory
from my_finance.models import StockModel
from my_finance.configuration.config import Configuration
from my_finance.database.stock_file_persistance import StockFilePersistance
from my_finance.database.stock_sql_persistance import StockSqlPersistance

app = Flask(__name__)

conf = Configuration()
print(conf.get_db_type())
if conf.get_db_type() == "file":
    print("file x 2")
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


@app.route("/stocks/<ticker>/delete", methods=["POST"])
def delete(ticker):
    stock_repo.remove(ticker)
    return redirect(url_for("hello"))


@app.route("/stocks", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        model = StockModel(ticker=request.form["ticker"])
        new_stock = StockFactory().make_from_model(model)
        stock_repo.add(new_stock)
        return redirect(url_for("hello"))
    if request.method == "GET":
        return render_template("add_new_stock.html")
