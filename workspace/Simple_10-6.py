# 錯誤-tuple無法修改
tuple_n = [31, 21, 54, 61]
print("tuple_n[2]:", tuple_n[2])
tuple_n[2] = 40

number_1 = (31, 21, 54, 61, 62)
print("初始資料 number_1:", number_1)
print("初始資料 number_1 型態", type(number_1))

number_2 = list(number_1)
print("資料 number_2:", number_2)
print("資料 number_1 型態", type(number_1))

number_3 = list(number_2)
print("資料 number_3:", number_3)
print("資料 number_3 型態", type(number_3))
