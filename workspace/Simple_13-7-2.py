def withdraw_1000():
    print("提領1000元程序")

def withdraw_3000():
    print("提領3000元程序")

def withdraw_5000():
    print("提領5000元程序")

withdraw = [withdraw_1000, withdraw_3000, withdraw_5000]
print("1.提領1000元程序\n2.提領3000元程序\n3.提領5000元程序")
ans = int(input("請輸入操作編號(1~3):")) - 1

if 0 <= ans <=2:
    withdraw[ans]()

else:
    print("error")
