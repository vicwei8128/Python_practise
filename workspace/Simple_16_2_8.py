file_a = open("file_name_XXX.txt", "a+")

print("1.\t 目前讀寫位置:", file_a.tell())
file_a.seek(0)
print("2.\t 目前讀寫位置:", file_a.tell())
print("-" * 20)
lines = file_a.readlines()

for i in lines:
    print(i, end="")

print("3.\t 目前讀寫位置:", file_a.tell())
file_a.write("cake\t60\n")
file_a.close()
