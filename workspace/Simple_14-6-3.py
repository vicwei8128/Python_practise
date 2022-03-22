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


class Flavor:
    def __init__(self, smell):
        self.smell = smell

    def get_smell(self):
        return "味道" + self.smell


class OriginDrink(Drink, Flavor):
    def __init__(self, name, price, country, variety, smell):
        super().__init__(name, price)
        # Drink.__init__(name, price)
        Flavor.__init__(self, smell)
        self.country = country
        self.variety = variety

    def get_country(self):
        return "產地" + self.country

    def get_variety(self):
        return "品種" + self.variety


class Company(OriginDrink):
    def __init__(self, company_name, name, price, country, variety, smell):
        super().__init__(name, price, country, variety, smell)
        self.company_name = company_name

    def get_company(self):
        return "銷售公司:" + self.company_name


drink = Company("一號店", "coffee", 100, "BM", "Arabica", "good")
dn = drink.get_name()
dp = drink.price_manage
dc = drink.get_country()
dv = drink.get_variety()
ds = drink.get_smell()
dcp = drink.get_company()

print(dcp, dv, dc, dn, "價格", dp, ds)
