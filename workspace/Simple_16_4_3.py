import json

file_a = open("file_name_JJJ.json", "r")
data = json.load(file_a)
print("data", data)
file_a.close()