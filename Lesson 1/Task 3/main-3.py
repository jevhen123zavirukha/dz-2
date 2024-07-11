# Task 3
import math


class ProperFraction:
    def __init__(self, numerator, denominator):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Numerator and denominator must be integers.")
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")

        self.numerator = numerator
        self.denominator = denominator
        self.reduce_fraction()

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def reduce_fraction(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __gt__(self, other):
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return ProperFraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return ProperFraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return ProperFraction(new_numerator, new_denominator)


fraction1 = ProperFraction(3, 5)
fraction2 = ProperFraction(4, 5)

print(f"first fraction: {fraction1}")
print(f"second fraction: {fraction2}\n")

print("Comparison:")
print(fraction1 < fraction2)
print(fraction1 > fraction2)
print(fraction1 == fraction2, "\n")

print("Addition:")
addition = fraction1 + fraction2
print(addition)

print("Subtraction:")
subtraction = fraction1 - fraction2
print(subtraction)

print("Multiplication:")
multiplication = fraction1 * fraction2
print(multiplication)
