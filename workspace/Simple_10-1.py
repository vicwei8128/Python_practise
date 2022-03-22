num = (31, 21, 54, 61, 62)
print("num", num)
print("type(num):", type(num))

name = ("coffee", "tea", "juice", "milk")
print("name", name)
print("type(name):", type(name))

num_1 = (31,)
num_2 = (31)
print("num_1", num_1)
print("num_2", num_2)
print("type(num_1):", type(num_1))
print("type(num_2):", type(num_2))

num_1 = ()
num_2 = tuple()
print("num_1", num_1)
print("num_2", num_2)
print("type(num_1):", type(num_1))
print("type(num_2):", type(num_2))

num = (31, 21, 54, 61, 62)
print("num[0]", num[0])
print("num[2]", num[2])
print("num[3]", num[3])
print("-" * 10)
print("num[-1]", num[-1])
print("num[-3]", num[-3])
print("num[-5]", num[-5])

num = (31, 21, 54, 61, 62)
print("length of tuple num", len(num))

num = (31, 21, 54, 61, 62)
for i in num:
    print(i)

num = (31, 21, 54, 67, 45, 21, 21)
print("出現次數:", num.count(21))
print("出現索引值", num.index(21))
print("出現次數:", num.count(54))
print("出現索引值", num.index(54))

num = (31, 21, 54, 61, 62, 55, 18, 63)
check_a = 55
check_b = 44
ans_a_in = check_a in num
ans_a_ni = check_a not in num
ans_b_in = check_b in num
ans_b_ni = check_b not in num
print("a_in", ans_a_ni)
print("a_ni", ans_a_ni)
print("b_in", ans_b_in)
print("b_ni", ans_b_ni)

num_1 = (31, 21, 54, 61, 62)
num_2 = (55, 18, 63, 72, 74)
conn = num_1 + num_2
print(conn)
num_1 += num_2
print(num_1)

num = (31, 21, 54, 61, 62, 55, 18, 63)
print("1.\t", num[2:7])
print("2.\t", num[:7])
print("3.\t", num[2:])
print("4.\t", num[2:7:2])
print("5.\t", num[::-1])

