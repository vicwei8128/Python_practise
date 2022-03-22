str_a = "coffee"
print("1.\t", str_a[0])
print("2.\t", str_a[1])
print("3.\t", str_a[2])
print("4.\t", str_a[3])
print("5.\t", str_a[-1])

str_a = "coffee"
print("1.\t", str_a[4])
print("2.\t", str_a[2:4])
print("3.\t", str_a[::-1])

str_a = "coffee"
for i in str_a:
    print(i)

str_a = "coffee"
print(len(str_a))


#無法將內部的值進行變更
str_a = "coffee"
print(str_a[3])
str_a[3] = "g"

str_a = "Pyt"
str_b = "hon"
str_c = str_b + str_a
print(str_c)