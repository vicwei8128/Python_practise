import os
import time

date = time.strftime("%Y%m%d", time.localtime())
dir_name = "dir_AAA" + date
path = "C:\Python_CFI102\workspace"

if dir_name not in os.listdir(path):
    os.mkdir(path + dir_name)