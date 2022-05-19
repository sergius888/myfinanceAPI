import unittest


def sum(x, y):
    return x + y


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_sums(self):
        self.assertEqual(5, 2 + 3)
        self.assertNotEqual(7, 8)
        self.assertFalse(5 > 9)

    def test_function_sum(self):
        # set up of fixture
        x = -10
        y = 9
        # execution
        s = sum(x, y)
        # assertion
        self.assertEqual(-1, s)
        # cleanup






if __name__ == '__main__':
    unittest.main()
