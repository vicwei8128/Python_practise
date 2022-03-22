file_a = open("file_name_XXX.txt", "r+")

data = ["joice\t 80\n", "milk\t 70\n"]
lines = file_a.readlines()
for i in lines:
    print(i,)
file_a.writelines(data)


file_a.close()

file_a = open("file_name_XXX.txt", "r+")

lines = file_a.readlines()
for i in lines:
    print(i, end="")

data = ["warer\t60\n", "milk\t110\n"]
file_a.writelines(data)

file_a.close()