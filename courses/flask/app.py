from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("hello.html")


@app.route("/stocks", methods=["GET", "POST"])
def stocks():
    print(request)
    if request.method == "GET":
        return "<h1>List of stocks:</h1>"
    elif request.method == "POST":
        return "aici o sa fie un formular"


@app.route("/stocks/<stock_id>")
def one_stock(stock_id: str):
    # we query the stock from database
    return render_template("one_stock.html", stock_id=stock_id, value=1000)