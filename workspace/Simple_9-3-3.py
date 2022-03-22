score = [98, 99, 87, 78, 56]

print("新增前的score資料:", score)
del score[2]
print("新增後的score資料:", score)


score = [98, 99, 87, 78, 56]

print("新增前的score資料:", score)
score.remove(99)
print("新增後的score資料:", score)

#錯誤示範

score = [98, 99, 87, 78, 56]

print("新增前的score資料:", score)
score.remove(100)
print("新增後的score資料:", score)


score = [98, 99, 87, 78, 56]

print("新增前的score資料:", score)
remove_value = 100
if remove_value in soure:
    score.remove(remove_value)
print("新增後的score資料:", score)