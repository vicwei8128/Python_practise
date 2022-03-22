number_1 = [98, 99, 87, 78, 56]
number_2 = [4, 9, 16]
number_new = number_1 + number_2
print("number_new:", number_new)

number_1 = [98, 99, 87, 78, 56]
number_2 = [4, 9, 16]
number_1.extend(number_2)
print("number_1:", number_1)

number_1 = [98, 99, 87, 78, 56]
number_2 = [4, 9, 16]
number_1 += number_2
print("number_1:", number_1)
