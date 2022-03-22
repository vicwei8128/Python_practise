# 錯誤-不可重複
product = {"coffee": 100, "tea": 90, "juice": 80, "juice": 70}
print(product)
print(type(product))

print("-" * 10)

product = {"coffee": "Africa", "tea": "Taiwan", "milk": "New Zealand"}
print(product)

print("-" * 10)

product = {5: "Africa", 6: "Taiwan", 8: "New Zealand"}
print(product)

print("-" * 10)

dict_a = {}
print("dict a:", dict_a)
print("type(dict a):", type(dict_a))
print("-" * 20)
dict_b = dict()
print("dict b:", dict_b)
print("type(dict b):", type(dict_b))

print("-" * 10)

product = {"coffee": 100, "tea": 90, "juice": 80, "milk": 70}
place = {5: "Africa", 6: "Taiwan", 8: "New Zealand"}
print("1.\t", product["juice"])
print("2.\t", place[6])

print("-" * 10)

product = {"coffee": 100, "tea": 90, "juice": 80, "milk": 70}
place = {15: "Africa", 6: "Taiwan", 8: "New Zealand"}
print("1.\tlen(product): ", len(product))
print("2.\tlen(place): ", len(place))

print("-" * 10)

product = {"coffee": 100, "tea": 90, "juice": 80}
product_k = product.keys()
product_v = product.values()
product_i = product.items()
print("1.\t", product_k)
print("2.\t", product_v)
print("3.\t", product_i)
print("-" * 10)
for i in product_k:
    print(i, end="\t")
print("\n" + "-" * 10)
for i in product_v:
    print(i, end="\t")
print("\n" + "-" * 10)
for i in product_i:
    print(i, end="\t")

print("-" * 10)

product = {"coffee": 100, "tea": 90, "juice": 80}
for i in product:
    print(i)
    print(product[i])

print("-" * 10)

product = {"coffee": 100, "tea": 90, "juice": 80}
ans_a = "coffee" in product
ans_b = "coffee" not in product
ans_c = "water" in product
ans_d = "water" not in product
print("1.\t", ans_a)
print("2.\t", ans_b)
print("3.\t", ans_c)
print("4.\t", ans_d)

print("-" * 10)

product = {"coffee": 100, "tea": 90, "juice": 80}
print("飲品名稱:coffee tea juice")
order = input("請輸入您想喝的飲品:")
if order in product:
    print("您點的飲品為:", order, "價格:", product[order])
else:
    print("很抱歉!菜單上沒有提供")

print("-" * 10)

product = {"coffee": 100, "tea": 90, "juice": 80}
print("1.\t", any(product))
print("2.\t", all(product))
product = {"coffee": 100, "tea": 90, "": 80}
print("3.\t", any(product))
print("4.\t", all(product))
product = {"": 80}
print("5.\t", any(product))
print("6.\t", all(product))

print("-" * 10)

number =[31, 21, 54, 61, 62]
print("1.\t", any(number))
print("2.\t", all(number))
number = [31, 21, 54, 61, 0]
print("3.\t", any(number))
print("4.\t", all(number))
number = [0]
print("5.\t", any(number))
print("6.\t", all(number))

print("-" * 10)

