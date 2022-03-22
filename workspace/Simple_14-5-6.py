class Drink:

    def __init__(self, name, price, discount):
        self.name = name
        self.price = price
        self.discount = discount

    def __calculate_discount(self):
        return self.price * self.discount

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price, self.__calculate_discount()


drink_1 = Drink("coffee", 100, 0.9)
n_1 = drink_1.get_name()
p_1, p_d_1 = drink_1.get_price()
print(n_1, "原價", p_1, "元\t特價", p_d_1, "元")
#t_1 = drink_1.__calculate_discount()

