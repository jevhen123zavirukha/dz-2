# Task 1
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('main.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


class PriceError(Exception):
    def __init__(self, message):
        super().__init__(message)


class Product:
    """
    Class for product
    """
    def __init__(self, name: str, price: int | float):
        """
        Initialize the product
        :param name: name of the product
        :param price: price of the product
        """
        if not isinstance(price, int | float):
            logger.error("Price must be an integer or float")
            raise TypeError("Price must be an integer or float")
        if price <= 0:
            logger.error("Price must be greater than 0")
            raise PriceError("Price must be greater than 0")

        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price} UAH"
