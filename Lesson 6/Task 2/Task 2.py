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


class OnlineWallet(PaymentMedia):
    def implement_a_payment(self, amount):
        print(f"Payment {amount} UAH. made using a online wallet.")


class PaymentProcessor:
    def __init__(self):
        self.payment_methods = []

    def add_payment_method(self, method):
        self.payment_methods.append(method)

    def make_a_payment(self, method_index, amount):
        if method_index < len(self.payment_methods):
            method = self.payment_methods[method_index]  # Fixed variable name
            method.implement_a_payment(amount)
        else:
            print("The selected payment method does not exist.")


if __name__ == "__main__":
    processor = PaymentProcessor()

    credit_card = CreditCard()
    bank_transfer = BankTransfer()
    online_wallet = OnlineWallet()

    processor.add_payment_method(credit_card)
    processor.add_payment_method(bank_transfer)
    processor.add_payment_method(online_wallet)

    processor.make_a_payment(0, float(input("Please enter the total amount: ")))
    processor.make_a_payment(1, float(input("\nPlease enter the total amount: ")))
    processor.make_a_payment(2, float(input("\nPlease enter the total amount: ")))
