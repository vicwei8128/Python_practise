operator_number = input("Please enter operator number(1~3):")

if operator_number == "1":
    #withdraw 1000 process
    print("提領1000元")
elif operator_number == "2":
    #withdraw 3000 process
    print("提領3000元")
elif operator_number == "3":
    #withdraw 5000 process
    print("提領5000元")
else:
    print("Please enter (1~3),no other number")
print("Program end")

score = float(input("Please enter score:"))
if score >= 60:
    print("及格")
elif score <= 60:
    print("不及格")
elif score == 0.0:
    print("0.0")
else:
    print("練習")

print("END")