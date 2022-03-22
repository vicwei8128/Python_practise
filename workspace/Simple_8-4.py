for i in range(1, 3+1, 1):
    for j in range(1, 3+1, 1):
        print("外圈i執行第", i,"次迴圈\t內圈j執行第", j, "次迴圈")
    print("-" * 10)
print("END")

i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print("外圈i執行第", i,"次迴圈\t內圈j執行第", j, "次迴圈")
        j += 1
    print("-" * 10)
    i += 1
print("END")

