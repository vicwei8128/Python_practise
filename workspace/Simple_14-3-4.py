class Drink:
    count = 0
    total_price = 0

    def __init__(self, name, price, discount):
        Drink.count = Drink.count + 1
        Drink.total_price = Drink.total_price + price * discount
        self.name = name
        self.price = price
        self.discount = discount

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price, self.price * self.discount


    @classmethod
    def get_count(cls):
        return cls.count

    @classmethod
    def get_total(cls):
        return cls.total_price


drink_1 = Drink("coffee", 100, 0.9)
n_1 = drink_1.get_name()
p_1, p_d_1 = drink_1.get_price()
print(n_1, "價格為", p_1, "元整\t特價後", p_d_1, "元整")

drink_2 = Drink("tea", 80, 0.8)
n_2 = drink_2.get_name()
p_2, p_d_2 = drink_2.get_price()
print(n_2, "價格為", p_2, "元整\t特價後", p_d_2, "元整")

print("合計", Drink.get_count(), "杯")
print("營業額", Drink.get_total(), "元")
