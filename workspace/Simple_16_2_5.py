file_a = open("file_name_XXX_3.txt", "x")

data = ["joice\t 80\n", "milk\t 70\n"]
file_a.writelines(data)

file_a.close()