name = {"嘉嘉", "喬喬", "厚厚", "富富", "星星"}
print(name)
print(type(name))
print("-" * 30)
company_id = [1001, 1002, 1003, 2003, 2033]
print(company_id)
print(type(company_id))

name = ["嘉嘉", "喬喬", "厚厚", "富富", "星星"]
print(name)
print(type(name))
name_s = set(name)
print("後來的資料:", name_s)
print("後來的資料型態:", type(name_s))

name = ("嘉嘉", "喬喬", "厚厚", "富富", "星星")
print(name)
print(type(name))
name_s = set(name)
print("後來的資料:", name_s)
print("後來的資料型態:", type(name_s))

data_a = set()
print(data_a)
print(type(data_a))
print("-" * 20)
data_b = {}
print(data_b)
print(type(data_b))

name_a = frozenset(("嘉嘉”,“喬喬", "厚厚", "富富", "星星"))
name_b = frozenset(["嘉嘉", "喬喬", "享厚", "富富", "星星"])
name_c = frozenset({"嘉嘉", "喬喬", "享厚", "富富", "星星"})
print("1.\t", name_a)
print("2.\t", name_b)
print("3.\t", name_c)
print("4.\t", type(name_a))
print("5.\t", type(name_b))
print("6.\t", type(name_c))

name = {"嘉嘉", "喬喬", "厚厚", "富富", "星星"}
print("length of name:", len(name))
for i in name:
    print("好久不見!" + i)

name = frozenset({"嘉嘉", "喬喬", "厚厚", "富富", "星星"})
for i in name:
    print("好久不見!" + i)

name = {"嘉嘉", "喬喬", "厚厚", "富富", "星星"}
ans_a = "幕幕" in name
ans_b = "幕幕" not in name
ans_c = "厚厚" in name
ans_d = "厚厚" not in name
print("1.\t", ans_a)
print("2.\t", ans_b)
print("3.\t", ans_c)
print("4.\t", ans_d)

name_a = {"嘉嘉", "喬喬", "厚厚", "富富", "星星", "望望"}
name_b = {"嘉嘉", "星星", "喬喬", "富富", "厚厚", "望望"}
name_c = {"嘉嘉", "喬香", "姿姿", "富富", "星星", "望望"}
ans_a = name_a == name_b
ans_b = name_a != name_b
ans_c = name_a == name_c
ans_d = name_a != name_c
print("1.\t", ans_a)
print("2.\t", ans_b)
print("3.\t", ans_c)
print("4.\t", ans_d)

name_a = {"嘉嘉", "喬喬", "厚厚", "富富"}
print("原本的資料:", name_a)
name_a.add("姿姿")
print("新增後的資料:", name_a)

name_a = {"嘉嘉", "喬喬", "厚厚", "富富", "星星"}
name_b = ("嘉嘉", "喬喬", "柏柏", "貴貴", "華華")
name_c = ("嘉嘉", "喬喬", "柏柏", "貴貴", "華華")
name_d = ["嘉嘉", "喬喬", "柏柏", "貴貴", "華華"]
name_e = {"嘉嘉": "0912345678", "喬喬": "09",
          "柏格": "09", "貴貴": "09", "華華": "09"}
print("聯集:", name_a.union(name_b))
print("交集:", name_a.intersection(name_c))
print("差集:", name_a.difference(name_d))
print("對稱差集:", name_a.symmetric_difference(name_e))
