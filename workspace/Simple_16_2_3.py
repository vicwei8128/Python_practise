file_a = open("file_name_XXX.txt")

data = file_a.readlines()

for i in data:
    j = i.split()
    print("飲品:{0:^8}價格為:{1}".format(j[0], j[1]))

file_a.close

file_a = open("file_name_XXX.txt", "r")

data = file_a.readline()
print(data)

file_a.close()