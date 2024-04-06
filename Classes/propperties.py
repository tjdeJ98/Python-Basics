class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    # Ugly = Unpythonic = Not using Pythons best practices

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be nagative.")
        self.__price = value

    @price.deleter
    def price(self):
        del (self.price)


product = Product(10)
product.price = 2
print(product.price)
del product
