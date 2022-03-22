import os
import stat

path_t_1 = "C:\\Python_CFI102\\workspace\\os_test"

os.chmod(path_t_1 + "\\a.txt", 0o700)
print("1.\t", os.stat(path_t_1 + "\\a.txt"))
print("2.\t", os.access(path_t_1 + "\\a.txt", os.W_OK))
print("3.\t", os.access(path_t_1 + "\\a.txt", os.R_OK))
print("4.\t", os.access(path_t_1 + "\\a.txt", os.X_OK))

os.chmod(path_t_1 + "\\a.txt", stat.S_IREAD)
print("5.\t", os.stat(path_t_1 + "\\a.txt"))
print("6.\t", os.access(path_t_1 + "\\a.txt", os.W_OK))
print("7.\t", os.access(path_t_1 + "\\a.txt", os.R_OK))
print("8.\t", os.access(path_t_1 + "\\a.txt", os.X_OK))

key = "OS"
value = os.getenv(key)
print("1.\t", value)

key = "Path"
value = os.getenv(key)
print("2.\t", value)