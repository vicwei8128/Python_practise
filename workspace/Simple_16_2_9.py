file_a = open("file_name_XXX.txt", "a+")

print("1.\t 目前讀寫位置:", file_a.tell())
file_a.write("oolong\t50\n")

print("2.\t 目前讀寫位置:", file_a.tell())
file_a.seek(0)
print("-" * 20)
lines = file_a.readlines()

for i in lines:
    print(i, end="")
file_a.close()
