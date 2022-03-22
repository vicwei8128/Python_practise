number = [98, 99, 87, 78, 56, 4, 9, 16]
number_1 = number[3:7]
print("1\t", number_1)
number_2 = number[:7]
print("2\t", number_2)
number_3 = number[3:]
print("3\t", number_3)
number_4 = number[3:7:2]
print("4\t", number_4)
number_5 = number[::-1]
print("5\t", number[::-1])

number = [98, 99, 87, 78, 56, 4, 9, 16]
print("原本的串列:", number)
number[3:7] = [100, 59, 49, 99]
print("修改後的串列", number)

number = [98, 99, 87, 78, 56, 4, 9, 16]
print("原本的串列:", number)
del number[3:7]
print("修改後的串列", number)