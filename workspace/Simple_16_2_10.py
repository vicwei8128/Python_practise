file_a = open("file_name_XXX.txt", "r")

data = file_a.read()
print(data)
file_a.close()

file_a = open("file_name_XXX.txt", "r")

data = file_a.read(20)
print(data)
file_a.close()
