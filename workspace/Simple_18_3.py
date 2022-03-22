import os.path

print("1.\t", os.listdir("./os_test"))
print("2.\t", os.path.abspath("."))
path_a = os.path.abspath(".")
print("3.\t", os.path.dirname(path_a))

path_b = "C:\\Python_CFI102\\workspace\\os_test"
print("4.\t", os.path.exists(path_b))
print("5.\t", os.path.dirname(path_b))
print("6.\t", os.path.basename(path_b))
print("7.\t", os.path.isdir(path_b))
print("8.\t", os.path.isfile(path_b))

path_c = "C:\\Python_CFI102\\workspace\\os_test"
print("9.\t", os.path.isdir(path_c))
print("10.\t", os.path.isfile(path_c))
print("11.\t", os.path.getsize(path_c))
print("12.\t", os.path.getatime(path_c))
print("13.\t", os.path.getmtime(path_c))
print("14.\t", os.path.getctime(path_c))