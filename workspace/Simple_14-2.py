class Drink:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price


drink_1 = Drink("coffee", 100)

n_1 = drink_1.get_name()
p_1 = drink_1.get_price()
print(n_1, "價格為", p_1, "元整")


class Drink:
    def __init__(self, name, price, discount):
        self.name = name
        self.price = price
        self.discount = discount

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price, self.price * self.discount


drink_1 = Drink("coffee", 100, 0.9)

n_1 = drink_1.get_name()
p_1, p_d_1 = drink_1.get_price()
print(n_1, "價格為", p_1, "元整\t特價後", p_d_1, "元整")
