from my_finance.stockk.stock import Stock
from my_finance.exceptions import StockNotFound, CannotAddStock, StockAlreadyAdded


class StockRepository:
    stocks = {}
    persistence = None



    @staticmethod
    def add(new_stock: Stock):
        stock_info = {
            "ticker": new_stock.ticker,
            "company": new_stock.company,
            "amount": new_stock.amount,
            "field": new_stock.field,
            "longSummary": new_stock.long_summary,
            "exchange": new_stock.exchange,
            "country": new_stock.country,
            "numberOfEmployees": new_stock.number_of_employees,
        }
        if new_stock.ticker not in StockRepository.stocks:
            try:
                StockRepository.persistence.add(stock_info)
            except Exception as e:
                raise CannotAddStock("Could not add stock. Reason: " + str(e))
            StockRepository.stocks[new_stock.ticker] = new_stock
        else:
            raise StockAlreadyAdded()

    @staticmethod
    def get_all() -> list[Stock]:
        print([s.price for s in StockRepository.stocks.values()])
        return list(StockRepository.stocks.values())

    # if we do not have the stock, we can raise an error or return None
    @staticmethod
    def get_by_ticker(ticker: str) -> Stock:
        if ticker in StockRepository.stocks.keys():
            return StockRepository.stocks[ticker]
        else:
            raise StockNotFound()
        # return StockFactory().make_extended_stock(ticker)



    @staticmethod
    def remove(stock_id: str):
        if stock_id in StockRepository.stocks.keys():
            StockRepository.stocks.pop(stock_id)
            StockRepository.persistence.remove(stock_id)
        else:
            raise StockNotFound()


    @staticmethod
    def load():
        items = StockRepository.persistence.get_all()
        # items = list of dictionaries from the file
        for one_item in items:
            new_stock = Stock(
                one_item["ticker"],
                one_item["company"],
                one_item["field"],
                one_item["country"],
                one_item["numberOfEmployees"],
                one_item["amount"],
            )
            if "longSummary" in one_item and "exchange" in one_item:
                new_stock.set_long_summary(one_item["longSummary"])
                new_stock.set_exchange(one_item["exchange"])
            StockRepository.stocks[one_item["ticker"]] = new_stock


    @staticmethod
    def edit_amount(ticker_id: str, amnt: float):
        if ticker_id in StockRepository.stocks.keys():
            StockRepository.persistence.update(ticker_id, amnt)
        else:
            raise StockNotFound()


    @staticmethod
    def add_transactions():
        pass



"""
add test with https://www.youtube.com/watch?v=IBJ6AeObUTg&list=LL&index=3&ab_channel=JJMusic
"""




list_of = [
  {
    "ticker": "FB",
    "company": "Meta Platforms, Inc.",
    "amount": 0,
    "current_value": 0,
    "transactions": [

    ],
    "field": "Communication Services",
    "longSummary": "Meta Platforms, Inc. develops products that enable people to connect and share with friends and family through mobile devices, personal computers, virtual reality headsets, wearables, and in-home devices worldwide. It operates in two segments, Family of Apps and Reality Labs. The Family of Apps segment's products include Facebook, which enables people to share, discover, and connect with interests; Instagram, a community for sharing photos, videos, and private messages, as well as feed, stories, reels, video, live, and shops; Messenger, a messaging application for people to connect with friends, family, groups, and businesses across platforms and devices through chat, audio and video calls, and rooms; and WhatsApp, a messaging application that is used by people and businesses to communicate and transact privately. The Reality Labs segment provides augmented and virtual reality related products comprising virtual reality hardware, software, and content that help people feel connected, anytime, and anywhere. The company was formerly known as Facebook, Inc. and changed its name to Meta Platforms, Inc. in October 2021. Meta Platforms, Inc. was incorporated in 2004 and is headquartered in Menlo Park, California.",
    "exchange": "NMS",
    "country": "United States",
    "numberOfEmployees": 77805
  }
]


# yal = 0
# xal = 0
# for y in list_of:
#     for l in y["transactions"]:
#         if l["position"] == "BUY":
#             xal += l["num_of_shares"] * l["at_price"]
#             yal += l["num_of_shares"]
#             # xal.append(l["num_of_shares"] * l["at_price"])
#             print(xal)
#         elif l["position"] == "SELL":
#             xal -= l["num_of_shares"] * l["at_price"]
#             yal -= l["num_of_shares"]
# print(xal)
#
# for x in list_of:
#     x["current_value"] = xal
#     x["amount"] = yal
#
# print(list_of)
#
# for x in list_of:
#     print(len(x["transactions"]))



from datetime import datetime

update = "mue"

for _ in range(1):
    if update == "yes":
        type_of = str(input("buy or sell "))

        amount_of = float(input("num of shares "))

        price_of = float(input("price "))
        now = datetime.now()
        date_of = now.strftime("%d/%m/%Y %H:%M:%S")

        dicsy = {
            "position": type_of.upper(),
            "num_of_shares": amount_of,
            "at_price": price_of,
            "transaction_date": date_of
        }

        for u in list_of:
            if len(u["transactions"]) > 0:
                for y in u["transactions"]:
                    print(type(y))
                    print(y)
                    print(type(u["transactions"]))
                    u["transactions"].append(dicsy)
                    break
            else:
                u["transactions"].append(dicsy)

    print(list_of)

    for x in list_of:
        print(len(x["transactions"]))



xxx =    [     {
            "position": "BUY",
            "num_of_shares": 25.5,
            "at_price": 200,
            "transaction_date": "01-06-2022",
            "asd" : [ {"position": "asd",
            "num_of_shares": 2.5,
            "at_price": 20,
            "transaction_date": "01-06-2022"} ]
        },
        {
            "position": "BUY",
            "num_of_shares": 30.0,
            "at_price": 190,
            "transaction_date": "09-06-2022"

        },
        {
            "position": "SELL",
            "num_of_shares": 25.0,
            "at_price": 220,
            "transaction_date": "01-07-2022"
        }
]

dicky = {
            "position": "BUY",
            "num_of_shares": 25.5,
            "at_price": 200,
            "transaction_date": "01-06-2022"
}

list_new = [
  {
    "ticker": "FB",
    "company": "Meta Platforms, Inc.",
    "amount": 0,
    "shares_value": 0,
    "field": "Communication Services",
    "longSummary": "Meta Platforms, Inc. develops products that enable people to connect and share with friends and family through mobile devices, personal computers, virtual reality headsets, wearables, and in-home devices worldwide. It operates in two segments, Family of Apps and Reality Labs. The Family of Apps segment's products include Facebook, which enables people to share, discover, and connect with interests; Instagram, a community for sharing photos, videos, and private messages, as well as feed, stories, reels, video, live, and shops; Messenger, a messaging application for people to connect with friends, family, groups, and businesses across platforms and devices through chat, audio and video calls, and rooms; and WhatsApp, a messaging application that is used by people and businesses to communicate and transact privately. The Reality Labs segment provides augmented and virtual reality related products comprising virtual reality hardware, software, and content that help people feel connected, anytime, and anywhere. The company was formerly known as Facebook, Inc. and changed its name to Meta Platforms, Inc. in October 2021. Meta Platforms, Inc. was incorporated in 2004 and is headquartered in Menlo Park, California.",
    "exchange": "NMS",
    "country": "United States",
    "numberOfEmployees": 77805,
    "transactions": [
        {
            "position": "BUY",
            "num_of_shares": 30.0,
            "at_price": 190,
            "transaction_date": "09-06-2022"

        },
        {
            "position": "SELL",
            "num_of_shares": 25.0,
            "at_price": 220,
            "transaction_date": "01-07-2022"
        }
    ]
  }
]
print("here starts")
print(list_new)


for dict in list_new:
    if dict["ticker"] == "FB":
        print("it is FB")
        if not len(dict["transactions"]) > 0:
            dict["transactions"].append(dicky)
        else:
            for key in dict["transactions"]:

                if len(dict["transactions"])>0:
                    dict["transactions"].append(dicky)
                    print(type(dict["transactions"]))
                    break




print(list_new)


        # print(type(y["asd"]))

