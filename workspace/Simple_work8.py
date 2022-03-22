# 8.作業1
i = 1
while i <= 9:
    j = 1
    while j <= 9:
        print(i, "*", j, "=", str(i * j))
        j += 1
    i += 1
print("END")

# 8.作業2
height = int(input("請輸入身高(公分):"))
weight = int(input("請輸入體重(公斤):"))
BMI = float(weight / (height / 100) ** 2)
print("您的身高:", height,
      "您的體重:", weight,
      "您的BMI值:", BMI)
if BMI < 18.5:
    print("體重過瘦")
elif 18.5 <= BMI < 24:
    print("體重標準")
elif 24 <= BMI < 27:
    print("體重過重")
elif 27 <= BMI < 30:
    print("輕度肥胖")
elif 30 <= BMI < 35:
    print("中度肥胖")
elif 35 <= BMI:
    print("重度肥胖")
i = 1
while i in range(2):
    rlp = int(input("請輸入代碼(1.繼續 2.停止):"))
    while rlp == 1:
        height = int(input("請輸入身高(公分):"))
        weight = int(input("請輸入體重(公斤):"))
        BMI = float(weight / (height / 100) ** 2)
        print("您的身高:", height,
              "您的體重:", weight,
              "您的BMI值:", BMI)
        if BMI < 18.5:
            print("體重過瘦")
        elif 18.5 <= BMI < 24:
            print("體重標準")
        elif 24 <= BMI < 27:
            print("體重過重")
        elif 27 <= BMI < 30:
            print("輕度肥胖")
        elif 30 <= BMI < 35:
            print("中度肥胖")
        elif 35 <= BMI:
            print("重度肥胖")
        break
    while rlp != 1 and rlp != 2:
        print("重新輸入")
        break
    if rlp == 2:
        print("已停止")
        break
