import json

from my_finance.stockk.persistence_interface import StockPersistanceInterface


class StockFilePersistance(StockPersistanceInterface):
    def __init__(self, path: str):
        self.path = path

    def get_all(self) -> list[dict]:
        print("get all")
        file = open(self.path)
        print("file opened")
        json_items = file.read()
        file.close()
        items = json.loads(json_items)
        return items

    def add(self, stock_info: dict):
        items = self.get_all()
        items.append(stock_info)
        self.__save(items)

    def __save(self, items: list[dict]):
        list_json = json.dumps(items, indent=2)
        file = open(self.path, "w")
        file.write(list_json)
        file.close()

    def remove(self, stock_id: str):
        items = self.get_all()
        items = [i for i in items if i["ticker"] != stock_id]
        self.__save(items)

    # Update the amount based on stock_id requested.
    def update(self, stock_id: str, amount: float):
        items = self.get_all()
        print("open file")
        for x in items:
            print("iterate")
            if stock_id in x.values():
                print("condition checks")
                x["amount"] += amount
        self.__save(items)

    def updt(self, stock_id: str, transaction_dictionary: dict):
        items = self.get_all()
        print("updt method opened file")
        for dict in items:
            if dict["ticker"] == stock_id:
                print(stock_id, "it is checked")
                if not len(dict["transactions"])>0:
                    dict["transactions"].append(transaction_dictionary)
                else:
                    for key in dict["transactions"]:
                        dict["transactions"].append(transaction_dictionary)
                        break
        self.__save(items)




transactions_info = [{
            "position": "BUY",
            "num_of_shares": 25,
            "at_price": 2,
            "transaction_date": "date_string"
        }
# {
#             "position": "SELL",
#             "num_of_shares": 30,
#             "at_price": 2,
#             "transaction_date": "date_string"
        ]
val_of_shares = 0
for i in transactions_info:
    if i["position"] == "BUY":
        val = i["num_of_shares"] * i["at_price"]
        val_of_shares += val
    elif i["position"] == "SELL":
        val = i["num_of_shares"] * i["at_price"]
        val_of_shares -= val
        if val_of_shares < 0:
            val_of_shares = 0
print(val_of_shares)
