import unittest
import logging.config


class CustomLogger(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.config.fileConfig('..\\Config\\config.ini', disable_existing_loggers=False)
        cls.logger = logging.getLogger('customLogger')

    def test_addition_of_two_numbers(self):
        val1 = 5
        val2 = 6
        result = add(val1, val2)
        self.logger.info(f'Addition of {val1}, {val2} is {result}')
        self.assertEqual(result, val1 + val2)

    def test_multiplication_of_two_numbers(self):
        val1 = 3
        val2 = 4
        result = multiply(val1, val2)
        self.logger.info(f'Multiplication of {val1}, {val2} is {result}')
        self.assertEqual(result, val1 * val2)


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


if __name__ == '__main__':
    unittest.main()
