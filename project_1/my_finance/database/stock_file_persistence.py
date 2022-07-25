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
            if stock_id in dict.values(): # TODO prevent TICKER from description - change to index of ticker
                for key in dict:
                    if len(key["transactions"]) > 0:
                        dict["transactions"].append(transaction_dictionary)
                        break




    # def update_db(self, amount: float):
    #     items = self.get_all()
    #     for x in items:
    #         x[amount] += amount
    #     self.__save(items)

#
# items = [
#   {
#     "ticker": "PATH",
#     "company": "UiPath Inc.",
#     "amount": 0,
#     "field": "Technology",
#     "longSummary": "UiPath Inc. provides an end-to-end automation platform that offers a range of robotic process automation (RPA) solutions primarily in the United States, Romania, and Japan. It develops UiPath Studio, a platform designed for RPA developers looking to build complex process automations with built-in governance capabilities, such as robust debugging tools, application programming interface automation, wizards to automate desktop or web applications, leverage custom code, and to integrate machine learning models into production workflows. The company also offers UiPath Robots, which emulates human behavior to execute the processes built in UiPath Studio; and UiPath Orchestrator that tracks and logs robot activity, along with what people do in tandem to maintain strict compliance and governance through dashboards and visualization tools. In addition, it provides maintenance and support for its software, as well as professional services, such as training and implementation services to facilitate the adoption of its platform. UiPath Inc. was founded in 2005 and is headquartered in New York, New York.",
#     "exchange": "NYQ",
#     "numberOfEmployees": 2863,
#     "country": "United States"
#   },
#   {
#     "ticker": "MSFT",
#     "company": "Microsoft Corporation",
#     "amount": 0,
#     "field": "Technology",
#     "longSummary": "Microsoft Corporation develops, licenses, and supports software, services, devices, and solutions worldwide. Its Productivity and Business Processes segment offers Office, Exchange, SharePoint, Microsoft Teams, Office 365 Security and Compliance, and Skype for Business, as well as related Client Access Licenses (CAL); Skype, Outlook.com, OneDrive, and LinkedIn; and Dynamics 365, a set of cloud-based and on-premises business solutions for organizations and enterprise divisions. Its Intelligent Cloud segment licenses SQL, Windows Servers, Visual Studio, System Center, and related CALs; GitHub that provides a collaboration platform and code hosting service for developers; and Azure, a cloud platform. It also offers support services and Microsoft consulting services to assist customers in developing, deploying, and managing Microsoft server and desktop solutions; and training and certification on Microsoft products. Its More Personal Computing segment provides Windows original equipment manufacturer (OEM) licensing and other non-volume licensing of the Windows operating system; Windows Commercial, such as volume licensing of the Windows operating system, Windows cloud services, and other Windows commercial offerings; patent licensing; Windows Internet of Things; and MSN advertising. It also offers Surface, PC accessories, PCs, tablets, gaming and entertainment consoles, and other devices; Gaming, including Xbox hardware, and Xbox content and services; video games and third-party video game royalties; and Search, including Bing and Microsoft advertising. It sells its products through OEMs, distributors, and resellers; and directly through digital marketplaces, online stores, and retail stores. It has collaborations with Dynatrace, Inc., Morgan Stanley, Micro Focus, WPP plc, ACI Worldwide, Inc., and iCIMS, Inc., as well as strategic relationships with Avaya Holdings Corp. and wejo Limited. Microsoft Corporation was founded in 1975 and is based in Redmond, Washington.",
#     "exchange": "NMS",
#     "country": "United States",
#     "numberOfEmployees": 181000
#   },
#   {
#     "ticker": "WMT",
#     "company": "Walmart Inc.",
#     "amount": 0,
#     "field": "Consumer Defensive",
#     "longSummary": "Walmart Inc. engages in the operation of retail, wholesale, and other units worldwide. The company operates through three segments: Walmart U.S., Walmart International, and Sam's Club. It operates supercenters, supermarkets, hypermarkets, warehouse clubs, cash and carry stores, and discount stores; membership-only warehouse clubs; ecommerce websites, such as walmart.com, walmart.com.mx, walmart.ca, flipkart.com, and samsclub.com; and mobile commerce applications. The company offers grocery and consumables, which includes dairy, meat, bakery, deli, produce, dry, chilled or frozen packaged foods, alcoholic and nonalcoholic beverages, floral, snack foods, candy, other grocery items, health and beauty aids, paper goods, laundry and home care, baby care, pet supplies, and other consumable items; and health and wellness products covering pharmacy, over-the-counter drugs and other medical products, and optical and hearing services. It also provides gasoline stations and tobacco; home improvement, outdoor living, gardening, furniture, apparel, jewelry, tools and power equipment, housewares, toys, seasonal items, mattresses, and tire and battery centers; and consumer electronics and accessories, software, video games, office supplies, appliances, and third-party gift cards. In addition, the company offers fuel and financial services and related products, including money orders, prepaid cards, money transfers, and check cashing and bill payment, as well as various types of installment lending. It operates approximately 10,500 stores and various e-commerce websites under 46 banners in 24 countries. The company was formerly known as Wal-Mart Stores, Inc. and changed its name to Walmart Inc. in February 2018. The company was founded in 1945 and is based in Bentonville, Arkansas.",
#     "exchange": "NYQ",
#     "country": "United States",
#     "numberOfEmployees": 2300000
#   },]
#
# stock_id = "PATH"
#
#
# def update_amount(self, stock_id: str):
#     for x in items:
#         if stock_id in x.values():
#             x.update()
#
# def edit_amount(ticker_id: str, amnt: float):
#     StockRepository.persistance.update(ticker_id, amnt)

# ers = "PATH"
#
# for x in items:
#     if x["ticker"] == ers:
#         print("yes")
#         x["amount"] += 15
#         print(x["amount"])
#
# print(items)

# def update_some(stock_info: dict):
#     # items = self.get_all()
#     for x in items:
#         if stock_info in x:
#             print("yes")
#             # x.update(stock_info)
#     # self.__save(items)
#
# ers = {"ticker": "PATH"}

# update_some(ers)




