import re

pattern_list = [r"^[0][9]\d{8}", r"^([A-Za-z][12])\d{8}]"]
search_list = ["0912345678", "a123456789", "A323456789"]

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


pattern_list = [r"^[0][9]\d{8}", r"^([A-Za-z][12])\d{8}]"]
search_list = ["0912345678", "a123456789", "A323456789"]

for pattern_value in pattern_list:
    pattern_var = re.compile(pattern_value)
    for search_value in search_list:
        result = pattern_var.search(search_value)
        print("模式:{0:^8},字串:{1:^8}".format(pattern_value, search_value), end="")
        if result is not None:
            print("匹配結果: OK")
            result_value = result.group()
            print("取得匹配到的資料:", result_value)
        else:
            print("匹配結果: NO")
        print("-" * 30)

pattern_list = [r"(news)\d{8}", r"(?<=news)\d{8}", "r(?<!news)\d"]
search_list = ["news0912345678abcda", "abcd20211010"]

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
