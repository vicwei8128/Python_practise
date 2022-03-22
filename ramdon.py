import random

n = random.randint(1, 4)
i = random.randint(1, 6)

if n == 1:
    print("北", "第", i, "間")
elif n == 2:
    print("南", "第", i, "間")
elif n == 3:
    print("西", "第", i, "間")
elif n == 4:
    print("東", "第", i, "間")


