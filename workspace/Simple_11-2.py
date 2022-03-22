product = {"coffee": 100, "tea": 90, "juice": 80}
print("原本資料:", product)
product["coffee"] = 99
print("變更後的資料:", product)


product = {"coffee": 100, "tea": 90, "juice": 80}
print("原本資料:", product)
product["milk"] = 70
print("新增後的資料:", product)


product_a = {"coffee": 100, "tea": 90, "juice": 80}
product_b = {"milk": 70, "water": 10, "coffee": 99}
print("更新前資料:", product_a)
product_a.update(product_b)
print("更新後資料:", product_a)


product = {"coffee": 100, "tea": 90, "juice": 80}
print("原本資料:", product)
del product["coffee"]
print("刪除後資料:", product)


product = {"coffee": 100, "tea": 90, "juice": 80}
print("原本資料:", product)
product.clear()
print("清除後資料:", product)


product = {"coffee": 100, "tea": 90, "juice": 80}
print("原本資料:", product)
data = product.pop("coffee")
print("data: ", data)
print("pop後資料:", product)


product = {"coffee": 100, "tea": 90, "juice": 80}
print("原本資料:", product)
data = product.popitem()
print("data: ", data)
print("pop後資料:", product)


product_a = {"coffee": 100, "tea": 90, "juice": 80}
product_b = product_a.copy()
product_b["coffee"] = 200
print("product a:", product_a)
print("product 6:", product_b)


product_a = {"coffee": 100, "tea": 90, "juice": 80}
product_b = dict(product_a)
product_b["coffee"] = 200
print("product a:", product_a)
print("product b:", product_b)

