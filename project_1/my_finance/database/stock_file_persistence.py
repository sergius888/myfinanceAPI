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

    # this method adds new transactions as a dict in a list of dicts, if conditions are checked
    # and it deletes everything if the amount of share owned is 0 and the last transaction is a SELL.
    def updt(self, stock_id: str, transaction_dictionary: dict, shares_val: float, amount: float):
        items = self.get_all()
        for dict in items:
            if dict["ticker"] == stock_id:
                dict["sharesCost"] += shares_val
                dict["amount"] += amount
                # below: add new transaction(as a dict) in transactions list
                if not len(dict["transactions"]) > 0:
                    dict["transactions"].append(transaction_dictionary)
                    # if the list contains 0 elements
                else:
                    for key in dict["transactions"]:
                        dict["transactions"].append(transaction_dictionary)
                        # iterate and add transaction if there is at least one already
                        break
                # below: if user sells all shares, it should clear the transactions list.
                # solution found is to check if the amount resulted is 0 but transaction list contains items.
                if dict["amount"] <= 0 and len(dict["transactions"]) > 0:
                    dict["transactions"].clear()
                    dict["amount"] = 0
                    dict["sharesCost"] = 0
                    dict["Potential P/L"] = 0
        self.__save(items)

    def update_profit_loss(self, ticker: str, price: float, time: str):
        items = self.get_all()
        for dict in items:
            if dict["amount"] > 0:
                if dict["ticker"] == ticker:
                    dict["Potential P/L"] = (dict["amount"] * price) - dict["sharesCost"]
                    x = round(dict["Potential P/L"], 2)
                    dict["Potential P/L"] = f'{x} $ \nas of {time}'
        self.__save(items)




"Potential P/L"




