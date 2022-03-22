file_a = open("file_name_XXX.txt", "a")

data = ["joice\t 80\n", "milk\t 70\n"]
file_a.writelines(data)

file_a.close()