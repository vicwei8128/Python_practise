str_a = "產品:{0}, 評價{1}".format("coffee", "*" * 5)
print(str_a)

str_a = "產品:{key_1}, 評價{key_2}".format(key_1="tea", key_2="good")
print(str_a)

number_of_vorters = 121
number_of_agree = 70
number_of_disagree = 20
vote_rate = (number_of_agree + number_of_disagree) / number_of_vorters * 100

str_ans = "投票人數:{0:^5},同意人數:{1:<5}, 不同意人數:{2:<5}, 投票率:{3:.10f}".format(number_of_vorters, number_of_agree,
                                                                       number_of_disagree, vote_rate)
print(str_ans)

number_of_vorters = 1234567890
str_ans = "投票人數:{0:,}".format(number_of_vorters)
print(str_ans)

number = 1234567890
str_ans = "{0}的2進位:{0:b},\n" \
          "{0}的8進位:{0:o},\n" \
          "{0}的10進位:{0:d},\n" \
          "{0}的16進位:{0:x},\n" \
          "{0}的指數標記:{0:e},\n".format(number)
print(str_ans)

number_of_vorters = 121
number_of_agree = 70
number_of_disagree = 20
vote_rate = (number_of_agree + number_of_disagree) / number_of_vorters * 100

info = {"number_of_vorters": number_of_vorters,
        "number_of_agree": number_of_agree,
        "vote_rate": vote_rate}
str_ans = "投票人數:{number_of_vorters}," \
          "同意人數:{number_of_agree}," \
          "投票率:{vote_rate:.2f}%".format(**info)
print(str_ans)

number_of_vorters = 121
number_of_agree = 70
number_of_disagree = 20
vote_rate = (number_of_agree + number_of_disagree) / number_of_vorters * 100

info = [number_of_vorters, number_of_agree, vote_rate]
str_ans = "投票人數:{0[0]},同意人數:{0[1]},投票率:{0[2]:.2f}%".format(info)
print(str_ans)

number_of_vorters = 121
number_of_agree = 70
number_of_disagree = 20
vote_rate = (number_of_agree + number_of_disagree) / number_of_vorters * 100

info = {number_of_vorters, number_of_agree, vote_rate}

str_ans_1 = f"投票人數:{number_of_vorters:^5},同意人數:{number_of_agree:<5}, 投票率:{vote_rate:.2f}%".format(number_of_vorters,
                                                                                                  number_of_agree,
                                                                                                  number_of_disagree,
                                                                                                  vote_rate)
print(str_ans_1)

str_ans_2 = F"投票人數:{number_of_vorters:^5},同意人數:{number_of_agree:<5}, 投票率:{vote_rate:.2f}%".format(number_of_vorters,
                                                                                                  number_of_agree,
                                                                                                  number_of_disagree,
                                                                                                  vote_rate)
print(str_ans_2)

str_a = "coffee"
str_b = "Tea"
str_c = "MILK"

print("1.{0:^20}取得大寫後{1}".format(str_a, str_a.upper()))
print("2.{0:^8}取得大寫後{1}".format(str_b, str_b.upper()))
print("3.{0:^8}取得大寫後{1}".format(str_b, str_b.lower()))
print("4.{0:^8}取得大寫後{1}".format(str_c, str_c.lower()))

str_a = "coffee"
str_b = "Tea"
str_c = "MILK"
print("1.{0:^8}首字大寫其餘小寫{1}".format(str_a, str_a.capitalize()))
print("2.{0:8}首字大寫其餘小寫{1}".format(str_b, str_b.capitalize()))
print("3.{0:^8}首字大寫其餘小寫{1}".format(str_c, str_c.capitalize()))
print("4.{0:8}大小寫互換{1}".format(str_a, str_a.swapcase()))
print("5.{0:8}大小寫互換{1}".format(str_b, str_b.swapcase()))
print("6.{0:8}大小寫互換{1}".format(str_c, str_c.swapcase()))

str_d = "MILK is good drink"
print("1.{0}每個單字字首轉成大寫{1}".format(str_d, str_d.title()))
print("2.{0}取得大寫後{1}".format(str_d, str_d.upper()))
print("3.{0}取得小寫後{1}".format(str_d, str_d.lower()))
print("4.{0}首字大寫其餘小寫{1}".format(str_d, str_d.capitalize()))
print("5.{0}大小寫互換{1}".format(str_c, str_c.swapcase()))

str_a = "--coffee--"
str_b = "  coffee  "
str_c = "1232coffec3232"
print("O.\t", str_a)
print("1.\t", str_a.strip("-"))
print("2.\t", str_a.lstrip("-"))
print("3.\t", str_a.rstrip("-"))
print("4.\t", str_b)
print("5.\t", str_b.strip())
print("6.\t", str_b.lstrip())
print("7.\t", str_b.rstrip())
print("8.\t", str_c)
print("9.\t", str_c.strip("123"))
print("10.\t", str_c.lstrip("123"))
print("11.\t", str_c.rstrip("123"))

str_a = "It's fun to stay at the Y.M.C.A."
str_b = "Python\nIs\tFun"
str_c = "0912-343-545"
print("1.\t", str_a.split())
print("2.\t", str_b.split())
print("3.\t", str_c.split("-"))
print("4.\t", str_a.split(" ", 2))
print("5.\t", str_c.split(" ", 1))

str_a = "It's fun to stay at the Y.M.C.A."
str_b = "It's fun\n to stay at the\n Y.M.C.A."
print("1.\t", str_a.splitlines())
print("2.\t", str_b.splitlines())
print("3.\t", str_b.splitlines(True))

list_c = ['0912', '343', '545']
str_a = ""
str_b = "-"
print("1.\t", str_a.join(list_c))
print("2.\t", str_b.join(list_c))

str_a = "It's fun to stay at the Y.M.C.A."
str_f = "to"
str_e = "ABC"

print("1.\t", str_a.find(str_f))
print("2.\t", str_a.find(str_f, 5))
print("3.\t", str_a.find(str_f, 5, 15))
print("4.\t", str_a.find(str_f, 10))
print("5.\t", str_a.find(str_e))

str_a = "This is an apple"
str_f = "a"
str_e = "ABC"
print("1.\t", str_a.rfind(str_f))
print("2.\t", str_a.find(str_f))
print("3.\t", str_a.rfind(str_f, 2, 15))
print("4.\t", str_a.rfind(str_f, 2, 10))
print("5.\t", str_a.rfind(str_e))

str_a = "This is an apple"
str_f = "a"
str_e = "ABC"

print("1.\t", str_a.index(str_f))
print("2.\t", str_a.index(str_f, 5, 7))

str_a = "ABC.txt.txt.txt.txt"
str_b = ".txt"
str_c = ".py"

print("1.\t", str_a.replace(str_b, str_c))
print("2.\t", str_a.replace(str_b, str_c, 1))
print("3.\t", str_a.replace(str_b, str_c, 3))

str_a = "ABC.txt.txt.txt.txt"
str_b = ".txt"
print("1.\t", str_a.count(str_b))
print("2.\t", str_a.count(str_b, 5))
print("3.\t", str_a.count(str_b, 5, 15))


str_a = "This is an apple"
str_b = "This"
str_c = "is"
print("1.\t", str_a.startswith(str_b))
print("2.\t", str_a.startswith(str_c))
print("3.\t", str_a.startswith(str_b, 5))
print("4.\t", str_a.startswith(str_c, 5))

str_a = "This is an apple"
str_b = "This"
str_c = "is"
print("1.\t", str_a.endswith(str_b))
print("2.\t", str_a.endswith(str_c))
print("3.\t", str_a.endswith(str_b, 5))
print("4.\t", str_a.endswith(str_c, 0, 4))

