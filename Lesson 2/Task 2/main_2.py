# Task 2
class Dish:
    def __init__(self, name: str, price: int | float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price} UAH"


class Category:
    def __init__(self, name: str):
        self.name = name
        self.__dishes = []

    def add_dish(self, dish: Dish):
        self.__dishes.append(dish)

    def __str__(self):
        dishes = "\n".join(map(str, self.__dishes))
        return f"{self.name}\n{dishes}"


class Menu:
    def __init__(self):
        self.__categories = []
        self.__index = 0

    def add_category(self, category: Category):
        self.__categories.append(category)

    def __str__(self):
        return "\n".join(map(str, self.__categories))

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index < len(self.__categories):
            category = self.__categories[self.__index]
            self.__index += 1
            return category
        raise StopIteration
