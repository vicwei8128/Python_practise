# 第七章作業
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