class ProductOriginal:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return "產品名稱" + self.name

    def get_price(self):
        return {"售價": self.price}


class ProductDiscount(ProductOriginal):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def get_discount_price(self):
        return {"特價:": self.price * self.discount}


product = ProductOriginal("coffee", 100)
p_gn = product.get_name()
p_gp = product.get_price()
print(p_gn, p_gp)
print("-" * 20)
product_2 = ProductDiscount("coffee", 100, 0.8)
p_gn2 = product_2.get_name()
p_gp2 = product_2.get_discount_price()
print(p_gn2, p_gp2)
