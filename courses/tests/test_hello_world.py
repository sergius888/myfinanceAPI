import unittest


def check_password(password: str):
    if password is None:
        raise Exception("You need to type a password!")
    if type(password) == bool:
        raise Exception("The password must be string!")
    return "strength: low"


class TestCheckPassword(unittest.TestCase):
    def test_there_if_password_none_raise_exception(self):
        # setup
        password = None
        with self.assertRaises(Exception) as context:  # assertion
            check_password(password)  # execution

        self.assertEqual("You need to type a password!", str(context.exception))  # assertion

    def test_password_is_string(self):
        # setup
        password = True
        # execution
        with self.assertRaises(Exception):
            check_password(password)
        # assertion
        # self.assertEqual("The password must be string!", output)

    def test_password_is_below_8_chars(self):
        # setup
        password = "short"
        # execution
        output = check_password(password)
        # assertion
        self.assertEqual("strength: low", output)