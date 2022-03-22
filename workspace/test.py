score = [98, 78, 87, 99, 78, 56, 78, 78]

i = int(input("請輸入:"))
while i in score:
    score.remove(i)
print(score)