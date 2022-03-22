class Drink:

    def __init__(self, name, price):
        self.name = name
        self.__price = price
        print("In class price:", self.__price)

    def get_price(self):
        print("---get price---")
        return self.__price

    def set_price(self, price):
        self.__price = price


drink_1 = Drink("coffee", 100)
print("1.\tdrink_1.get_price", drink_1.get_price())

drink_1.set_price(200)
print("2.\tdrink_1.set_price", drink_1.get_price())