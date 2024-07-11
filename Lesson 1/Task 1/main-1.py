# Task 1


class Product:
    def __init__(self, name: str, price: int | float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price} UAH"


class Cart:

    def __init__(self):
        self.__products = []
        self.__quantities = []

    def add_product(self, product: Product, quantity: int | float = 1):
        if product in self.__products:
            index = self.__products.index(product)
            self.__quantities[index] += quantity
        else:
            self.__products.append(product)
            self.__quantities.append(quantity)

    def total(self):
        res = 0
        for product, quantity in zip(self.__products, self.__quantities):
            res += product.price * quantity
        return res

    def __iadd__(self, other):
        if isinstance(other, Cart):
            self.__products.extend(other.__products)
            self.__quantities.extend(other.__quantities)
        return self

    def __str__(self):
        res = '\n'.join(map(lambda item: f"{item[0]} x {item[1]} = {item[0].price * item[1]} UAH",
                            zip(self.__products, self.__quantities)))
        res += f"\nTotal: {self.total()} UAH"
        return res
