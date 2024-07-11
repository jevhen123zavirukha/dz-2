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

    def add_category(self, category: Category):
        self.__categories.append(category)

    def __str__(self):
        return "\n".join(map(str, self.__categories))


class Order:
    def __init__(self):
        self.__dishes = []

    def __iadd__(self, dish: Dish):
        self.__dishes.append(dish)
        return self

    def __str__(self):
        return "\n".join(map(str, self.__dishes))


dish_1 = Dish("Pizza", 10)
dish_2 = Dish("Pasta", 15)
dish_3 = Dish("Salad", 5)
dish_4 = Dish("Soup", 3)
dish_5 = Dish("Steak", 20)
dish_6 = Dish("Burger", 7)

category_1 = Category("Main Course")
category_1.add_dish(dish_1)
category_1.add_dish(dish_2)
category_1.add_dish(dish_3)

category_2 = Category("Appetizer")
category_2.add_dish(dish_4)
category_2.add_dish(dish_5)
category_2.add_dish(dish_6)

menu = Menu()
menu.add_category(category_1)
menu.add_category(category_2)

order = Order()

print(menu, "\n")

order += dish_1
order += dish_2
order += dish_3

print("\nOrder:")
print(order, "\n")
