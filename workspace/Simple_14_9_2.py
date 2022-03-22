class Origin:

    def __init__(self, country, variety, company_name):
        self.country = country
        self.variety = variety
        self.company_name = company_name

    def get_country(self):
        return "產地" + self.country

    def get_variety(self):
        return "品種" + self.variety

    def get_company(self):
        return "銷售公司:" + self.company_name

class Company(Origin):
    def __init__(self, country, variety, company_name):
        super().__init__(country, variety, company_name)

    def get_company(self):
        return "銷售分店:" + self.company_name


drink = Company("一號店", "BM", "Arabica")
dc = drink.get_country()
dv = drink.get_variety()
dcp = drink.get_company()

print(dcp, dv, dc)
