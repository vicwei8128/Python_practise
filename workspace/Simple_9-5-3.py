number = [4, 9, 16, 25, 36, 49]
print("原本的串列:", number)
rev_number = number[::-1]
print("逆向後的number資料:", number)
print("逆向後的rev_number資料:", rev_number)

number = [4, 9, 16, 25, 36, 49]
print("原本的number:", number)
number.reverse()
print("逆向的number:", number)

number = [4, 9, 16, 25, 36, 49]
print("原本的nuber:", number)
rev_number = reversed(number)
print("逆向後的number:", number)
print("逆向後的rev_number:", rev_number)
for i in rev_number:
    print(i)
