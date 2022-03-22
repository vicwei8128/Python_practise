product_name = ["coffee", "tea", "juice", "milk"]
product_price = [100, 90, 80, 70]

for name, price in zip(product_name, product_price):
    print('商品名稱:', name, "價格", price)