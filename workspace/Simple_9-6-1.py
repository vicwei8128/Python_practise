product_name = ["coffee", "tea", "juice", "milk"]
product_price = [100, 90, 80, 70]

for i in zip(product_name, product_price):
    print(i)

product_name = ["coffee", "tea", "juice", "milk"]
product_price = [100, 90, 80]

for i in zip(product_name, product_price):
    print(i)

product_name = ["coffee", "tea", "juice", "milk"]
product_price = [100, 90, 80, 70]

for i in zip(product_name, product_price):
    print(i)
    print(type(i))

product_name = ["coffee", "tea", "juice", "milk"]

for i in enumerate(product_name):
    print(i)

score = [98, 99, 87, 78, 56, 78, 78]
look_for = 78
for i in enumerate(score):
    if i[1] == look_for:
        print("index of", look_for, "is:", i[0])
