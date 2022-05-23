import unittest
from unittest.mock import Mock

from my_finance.exceptions import CannotAddStock
from my_finance.stock.stock_repo import StockRepository
from my_finance.stock.stock import Stock


class StockRepoTest(unittest.TestCase):
    # this function will execute before each test
    def setUp(self) -> None:
        # set up
        self.persistance_mock = Mock()
        # persistance_mock.add()
        StockRepository.persistance = self.persistance_mock

    def tearDown(self) -> None:
        # cleanup/teardown
        StockRepository.stocks = {}

    # this function will execute before anything else and only 1 time, it is optional
    @classmethod
    def setUpClass(cls) -> None:
        print("set up class")

    def test_add(self):
        new_stock = Stock("TSLA", "Tesla Inc.", "Technology", "USA", 99000)
        # execution
        StockRepository.add(new_stock)
        # assertion
        self.assertIn(new_stock, StockRepository.stocks.values())
        self.assertCountEqual([new_stock], StockRepository.stocks.values())
        self.persistance_mock.add.assert_called_once()

    def test_exception_at_add(self):
        new_stock = Stock("TSLA", "Tesla Inc.", "Technology", "USA", 99000)
        self.persistance_mock.add.side_effect = Exception("error message")
        # execution
        with self.assertRaises(CannotAddStock):
            StockRepository.add(new_stock)
        self.assertCountEqual([], StockRepository.stocks.values())


if __name__ == "__main__":
    unittest.main()
