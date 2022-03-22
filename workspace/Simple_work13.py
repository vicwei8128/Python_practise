# 13.實作

def fun(n):
    if n <= 1:
        return 1
    elif n > 1:
        return fun(n - 2) + fun(n - 1)


# print(fun(n-2) + fun(n - 1))
data = int(input("請問要做到費氏數列第幾項?"))
for i in range(data):
    print(fun(i), end=",")
