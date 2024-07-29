# Task 2
from abc import ABC, abstractmethod


class PaymentMedia(ABC):
    @abstractmethod
    def implement_a_payment(self, amount):
        pass


class CreditCard(PaymentMedia):
    def implement_a_payment(self, amount):
        print(f"Payment {amount} UAH. made using a credit card.")


class BankTransfer(PaymentMedia):
    def implement_a_payment(self, amount):
        print(f"Payment {amount} UAH. made using a bank transfer.")
