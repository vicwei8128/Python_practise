import re

pattern_list = ["coffee", "tea"]
search_list = ["coffee", "milk"]

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