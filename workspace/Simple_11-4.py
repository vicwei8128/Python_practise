product = {"coffee": 100, "tea": 90, "juice": 80, "milk": 70, "water": 10}
print("產品名稱:", product)
new_product_price = {i: int(product[i] * 0.95) if product[i] > 80 else
int(product[i] * 0.8) if 20 < product[i] <= 80 else
int(product[i] * 0.1)
                     for i in product}
print("全面商品大優惠--優惠最大是1折--")
print("打折後價格", new_product_price)
