import unittest
from error_handler import ErrorHandler


class TestErrorHandler(unittest.TestCase):
    def test_raising(self):
        with self.assertRaises(AttributeError):
            ErrorHandler.throw_error(AttributeError)


if __name__ == '__main__':
    unittest.main()
