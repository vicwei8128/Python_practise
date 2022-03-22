import re

pattern_list = ["[012]", "[^012]]"]
search_list = ["1", "12", "3"]

for pattern_value in pattern_list:
    pattern_var = re.compile(pattern_value)
    for search_value in search_list:
        result = pattern_var.search(search_value)
        print("模式:{0:^8},字串:{1:^8}".format(pattern_value, search_value), end="")
        if result is not None:
            print("匹配結果: OK")
        else:
            print("匹配結果: NO")
        print("-" * 30)


pattern_list = ["[abc]", "[^abc]]"]
search_list = ["a", "A", "a123"]

for pattern_value in pattern_list:
    pattern_var = re.compile(pattern_value)
    for search_value in search_list:
        result = pattern_var.search(search_value)
        print("模式:{0:^8},字串:{1:^8}".format(pattern_value, search_value), end="")
        if result is not None:
            print("匹配結果: OK")
        else:
            print("匹配結果: NO")
        print("-" * 30)
