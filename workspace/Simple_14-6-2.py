class Drink:

    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def get_name(self):
        return self.name

    @property
    def price_manage(self):
        return self.__price

    @price_manage.setter
    def price_manage(self, price):
        self.__price = price


class OriginDrink(Drink):
    def __init__(self, name, price, country, variety):
        super().__init__(name, price)
        # Drink.__init__(name, price)
        self.country = country
        self.variety = variety

    def get_country(self):
        return "產地" + self.country

    def get_variety(self):
        return "品種" + self.variety


drink = OriginDrink("coffee", 100, "BM", "Arabica")
dn = drink.get_name()
dp = drink.price_manage
dc = drink.get_country()
dv = drink.get_variety()

print(dv, dc, dn, "價格", dp)
