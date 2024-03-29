from flask import Flask, render_template, redirect, url_for, request, json
from my_finance.exceptions import StockAlreadyAdded
from my_finance.stockk.stock_repo import StockRepository
from my_finance.stockk.stock_factory import StockFactory
from my_finance.models import StockModel
from my_finance.configuration.config import Configuration
from my_finance.database.stock_file_persistence import StockFilePersistance
from my_finance.database.stock_sql_persistence import StockSqlPersistance

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


conf = Configuration()
print(conf.get_db_type())

if conf.get_db_type() == "file":
    print("file x 2")
    persistence = StockFilePersistance(conf.get_db_path())
if conf.get_db_type() == "sql":
    persistence = StockSqlPersistance(conf.get_db_path())
StockRepository.persistence = persistence
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


@app.route("/stocks/<ticker>/transactions", methods=["GET", "POST"])
def update_amount(ticker):
    items = persistence.get_all()
    transactions = [x for stocks in items if stocks["ticker"] == ticker for x in stocks["transactions"]]
    transactions = list(reversed(transactions))

    if request.method == "POST":
        if request.form["submit_button"] == "Buy":
            position = "BUY"
        else:
            print("works with sell")
            position = "SELL"

        u = request.form.get('shares_text')
        num_of_shares = float(u)
        stock_repo.add_transactions(ticker, position, num_of_shares)
        return render_template("transactions_history.html", transactions=transactions, ticker=ticker)

    if request.method == "GET":
        return render_template("transactions_history.html", transactions=transactions, ticker=ticker)


@app.route("/stocks", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        model = StockModel(ticker=request.form["ticker"])
        new_stock = StockFactory().make_from_model(model)
        try:
            stock_repo.add(new_stock)
            return redirect(url_for("hello"))
        except:
            return render_template("error_display.html", company=new_stock.company,
                                   ticker=new_stock.ticker)

    if request.method == "GET":
        return render_template("add_new_stock.html")


# @app.route("/stocks/<ticker>/read", methods=["POST"])
# def some_name(ticker):


'''
TODO add update PL button (instead of restarting with when server starts)

'''