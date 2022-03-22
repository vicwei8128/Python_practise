for i in range(6):
    print("正在執行", i)
print("Program end")

for i in range(1,6):
    print("正在執行", i)
print("Program end")

for i in range(1,6+1):
    print("正在執行", i)
print("Program end")

for i in range(1,6+1,1):
    print("正在執行", i)
print("Program end")

for i in range(1,6+1,2):
    print("正在執行", i)
print("Program end")

for i in range(1,6+1,3):
    print("正在執行", i)
print("Program end")

for i in range(6,0,-1):
    print("正在執行", i)
print("Program end")

for i in range(6,0,-2):
    print("正在執行", i)
print("Program end")

j = 0
for i in range (0, 10+1, 1):
    print("j",j ,"i",i)
    j += i

print("Total j:",j)

for i in range(1,6,1):
    if (i % 2) ==0:
        print(i, "is even")
    else:
        print(i, "is odd")
print("program end")