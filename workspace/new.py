#socre = [98, 78, 87, 99, 78, 56, 78, 78]
socre = [98, 99, 87, 78, 56, 78, 78]

x = input("請輸入:")

for num in socre[:]:
    socre.remove(int(x))
    print(socre)
