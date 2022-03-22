file_a = open("file_name_XXX.txt", "w")

file_a.write("coffee\t 100\n")
file_a.write("tea\t 80\n")
file_a.close()

file_a = open("file_name_XXX.txt", "w")

data = ["coffee\t 100\n", "tea\t 80\n"]
file_a.writelines(data)

file_a.close()
