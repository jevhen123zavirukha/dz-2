# Task 2
from abc import ABC, abstractmethod


class PaymentMedia(ABC):
    @abstractmethod
    def implement_a_payment(self, amount):
        pass

