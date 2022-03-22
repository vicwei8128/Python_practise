# 14.實作

def calculate_bmi(h, w):
    BMI = float(w / (h / 100) ** 2)
    return BMI


height = float(input("請輸入身高(cm):"))
weight = float(input("請輸入體重(kg):"))

BMI = calculate_bmi(height, weight)
print("身高:", height, "體重:", weight)
print("BMI:", BMI)
