# A deposit method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.
# A withdraw method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise.
# A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
# A transfer method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
# A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.

# Complete the Category class in budget.py. It should be able to instantiate objects based on different budget categories like food, clothing, and entertainment. When objects are created, they are passed in the name of the category. The class should have an instance variable called ledger that is a list.

class Budget:
    def __init__(self, ledger):
        self.ledger = ledger

    def deposit(self, amount, description=""):
        self.ledger = {"amount": amount, "description": description}
        return self.ledger

    def withdraw(self):
        pass

    def get_balance(self):
        pass

    def transfer(self):
        pass

    def check_funds(self):
        pass

# asc = Budget("something")
#
# print(asc.deposit(23, "somethings"))

dict = []

list1 = {"shit": "asd"}
list2 = {"shites": "asde"}
list3 = {"st": "a"}


