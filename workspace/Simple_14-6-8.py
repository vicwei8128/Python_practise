class Drink:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        dr = self.name + "\t好喝"
        return dr

    def __int__(self):
        price = self.price
        return price

    def __add__(self, other):
        price = self.price + other.price
        return price

drink = Drink("coffee", 100)
print(str(drink))
print(int(drink))
drink_2 = Drink("tea", 90)
print(str(drink_2))
print(int(drink_2))
print("總額:", drink_2 + drink)