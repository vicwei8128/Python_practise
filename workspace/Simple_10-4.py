product_name = ("coffee", "tea", "juice", "milk")
product_price = (100, 90, 80, 70)

for i in zip(product_name, product_price):
    print(i)

product_name = ("coffee", "tea", "juice", "milk")

for i in enumerate(product_name):
    print(i)

product_name = ("coffee", "tea", "juice", "milk")
product_price = (100, 90, 80, 70)
for i, j in zip(product_name, product_price):
    print("商品", i, "價格", j)

product_name = ("coffee", "tea", "juice", "milk")
product_price = (100, 90, 80, 70)
n_p_1, n_p_2, n_p_3, n_p_4 = zip(product_name, product_price)
print("1.\t", n_p_1)
print("2.\t", n_p_2)
print("3.\t", n_p_3)
print("4.\t", n_p_4)
