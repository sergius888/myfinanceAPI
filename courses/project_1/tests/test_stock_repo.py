import unittest
from unittest.mock import Mock


from my_finance.stock_repo import StockRepository
from my_finance.stock.stock import Stock

class StockRepoTest(unittest.TestCase):
    def setUp(self) -> None:
        print("set up simple")

    # test function will execute before anything else and only 1 time, it is optional
    @classmethod
    def setUpClass(cls) -> None:
        print("set up class")

    def test_add(self):
        # set up
        persistance_mock = Mock()
        StockRepository.persistance = persistance_mock
        new_stock = Stock("TSLA", "Tesla Inc", "Technology", "USA", 99000)
        # execution
        StockRepository.add(new_stock)
        # assertion
        self.assertIn(new_stock, StockRepository.stocks.values)
        self.assertCountEqual([new_stock], StockRepository.stocks)
        # clean up
        StockRepository.stocks = {}



    def test_2(self):
        self.assertEqual(True, False)



if __name__ == '__main__':
    unittest.main()
