import json

try:
    file_a = open("file_name_JJJ.json", "r")
except FileNotFoundError as er_name:
    print(er_name)
    print("please check your file.")

else:
    data = json.load(file_a)
    print(data["drink"][0])
    file_a.close()

finally:
    print("END")


try:
    file_a = open("file_name_JJ.json", "r")
except FileNotFoundError as er_name:
    print(er_name)
    print("please check your file.")

else:
    data = json.load(file_a)
    print(data["drink"][0])
    file_a.close()

finally:
    print("END")


def read_jshon(file_name):
    file_a = open(file_name, "R")
    da = json.load(file_a)
    file_a.close()

