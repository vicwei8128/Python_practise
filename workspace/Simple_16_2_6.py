file_a = open("file_name_XXX_4.txt", "w+")

data = ["joice\t 80\n", "milk\t 70\n"]
file_a.writelines(data)
file_a.seek(0)
lines = file_a.readlines()

for i in lines:
    j = i.split()
    print("飲品:{0:^8}價格為:{1}".format(j[0], j[1]))

file_a.close()

file_a = open("file_name_XXX_4.txt", "w+")

print("1.\t 目前讀寫位置:", file_a.tell())
data = ["joice\t 80\n", "milk\t 70\n"]
file_a.writelines(data)
print("2.\t 目前讀寫位置:", file_a.tell())
file_a.seek(0)
print("3.\t 目前讀寫位置:", file_a.tell())
lines = file_a.readlines()

for i in lines:
    j = i.split()
    print("飲品:{0:^8}價格為:{1}".format(j[0], j[1]))

print("4.\t 目前讀寫位置:", file_a.tell())
file_a.close()

