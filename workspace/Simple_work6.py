# 第六章作業
height = int(input("請輸入身高(公分):"))
weight = int(input("請輸入體重(公斤):"))
BMI = float(weight / (height / 100) ** 2)
print("您的身高:", height,
      "您的體重:", weight,
      "您的BMI值:", BMI)
