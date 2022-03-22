import os
import stat

print("現在目錄:", os.getcwd())

path_t_1 = "C:\\Python_CFI102\\workspace\\os_test"
print("1.\t", os.listdir(path_t_1))

path_t_2 = "C:\\Python_CFI102\\workspace\\os_test"
print("2.\t", os.listdir(path_t_2))

path_t_1 = "C:\\Python_CFI102\\workspace\\os_test"
print("1.\t", os.listdir(path_t_1))
os.remove(path_t_1 + "\\d.txt")
print("2.\t", os.listdir(path_t_1))

path_t_1 = "C:\\Python_CFI102\\workspace\\os_test"
print("1.\t", os.listdir(path_t_1))
os.mkdir(path_t_1 + "\\a_dir_name")
print("2.\t", os.listdir(path_t_1))

path_t_1 = "C:\\Python_CFI102\\workspace\\os_test"
print("1.\t", os.listdir(path_t_1))
os.rename(path_t_1 + "\\a_dir_name", path_t_1 + "\\b_dir_name")
print("2.\t", os.listdir(path_t_1))

path_t_1 = "C:\\Python_CFI102\\workspace\\os_test"
print("1.\t", os.listdir(path_t_1))
os.rmdir(path_t_1 + "\\b_dir_name")
print("2.\t", os.listdir(path_t_1))

path_t_1 = "C:\\Python_CFI102\\workspace\\os_test"
print("1.\t", os.access(path_t_1 + "\\a.txt", os.F_OK))
print("2.\t", os.access(path_t_1 + "\\a.txt", os.W_OK))
print("3.\t", os.access(path_t_1 + "\\a.txt", os.R_OK))
print("4.\t", os.access(path_t_1 + "\\a.txt", os.X_OK))

print("5.\t", os.access(path_t_1 + "\\d.txt", os.F_OK))

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
