score = [98, 99, 87, 78, 56]

for i in score:
    if i > 100:
        print("number is", i)
        break
else:
    print("No element bigger than 100")

score = [98, 99, 87, 110, 78, 56]

for i in score:
    if i > 100:
        print("number is", i)
        break
else:
    print("No element bigger than 100")


score = [98, 99, 87, 78, 56]
i = 0
while i < len(num):
    if num[i] > 100:
        print("number is", num[i])
        break
    i += 1
else:
    print("No element bigger than 100")

score = [98, 99, 87, 78, 56, 110]
i = 0
while i < len(num):
    if num[i] > 100:
        print("number is", num[i])
        break
    i += 1
else:
    print("No element bigger than 100")