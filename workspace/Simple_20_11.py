import re

pattern_str = r"(\.txt)"
dir_list = ["AAA.py", "BBB.exe", "CCC.txt", "DDD.txt"]
pattern_var = re.compile(pattern_str)
for dir_name in dir_list:
    result = pattern_var.sub(".py", dir_name)
    print("轉換前名稱{0:^11}, 轉換後的名稱{1:^11}".format(dir_name, result))