import pytest
import logging, logging.config


@pytest.fixture(scope='session')
def custom_logger():
    logging.config.fileConfig(fname=r'../Config/config.ini', disable_existing_loggers=False)
    logger = logging.getLogger('customLogger')
    return logger


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def test_addition_of_two_numbers(custom_logger):
    logger = custom_logger

    val1 = 5
    val2 = 6
    result = add(val1, val2)
    logger.info(f'Addition of {val1}, {val2} is {result}')
    assert result == val1 + val2


def test_multiplication_of_two_numbers(custom_logger):
    logger = custom_logger

    val1 = 3
    val2 = 4
    result = multiply(val1, val2)
    logger.info(f'Multiplication of {val1}, {val2} is {result}')

    assert result == val1 * val2
