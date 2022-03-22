stop_condition = int(input("請輸入做到第幾迴圈時要跳出迴圈(1~100):"))

for i in range(1,100+1,1):
    print("目前做到第",i,"圈",end="\t")
    if i == stop_condition:
        break
    print("Do something process.")

print()
print("END")
