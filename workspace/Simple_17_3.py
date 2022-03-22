import json


def read_json(file_name):
    file_a = open(file_name, "r")
    da = json.load(file_a)
    file_a.close()
    return da["table"]


class MyNameIsException(BaseException):
    def __init__(self, num, message):
        self.num = num
        self.message = message

    def __str__(self):
        return self.num + "\t" + self.message


try:
    data = read_json("file_name_JJJ.json")
    print(data[1:])
    try:
        table_num = input("Please enter table(1~5):")
        if table_num not in ["1", "2", "3", "4", "5"]:
            raise MyNameIsException(table_num, "is not 0~5")
        print(data[int(table_num)])
    except MyNameIsException as er_name:
        print(er_name)
except FileNotFoundError as er_name:
    print(er_name)
    print("please check your file.")
