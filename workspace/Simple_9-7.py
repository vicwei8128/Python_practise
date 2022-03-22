product_price = [100, 90, 80, 70]
print("product price:", product_price)
new_product_price = [i * 0.9 for i in product_price if 70 < i <= 90]
print("new product price:", new_product_price)

product_name = ["coffee", "tea", "juice", "milk"]
product_price = [100, 90, 80, 70]
print("產品名稱:", product_name)
print("產品價格:", product_price)
new_product_price = [i * 0.5 for i in product_price]
print("-- --全面商品五折優惠-- ---")
print("打折後價格", new_product_price)

product_name = ["coffee", "tea", "juice", "milk", "water"]
product_price = [100, 90, 80, 70, 10]
print("產品名稱:", product_name)
print("產品價格:", product_price)
new_product_price = [int(i * 0.5) if i <= 70 else int(i * 0.9) for i in product_price]
print("-- 一全面商品折優惠--部分商品五折優惠")
print("打折後價格", new_product_price)

product_name = ["coffee", "tea", "juice", "milk", "water"]
product_price = [100, 90, 80, 70, 10]
print("產品名稱:", product_name)
print("產品價格:", product_price)
new_product_price = [int(i * 0.95) if i > 80 else
                     int(i * 0.8) if 20 < i <= 80 else
                     int(i*0.1)
                     for i in product_price]
print("--全面商品大優惠--優惠最大是1折--")
print("打折後價格", new_product_price)
