ans = (lambda x: x * 0.8)(100)
print("ans", ans)

discount = (lambda x: x*0.8)
print(discount(100))
print(type(discount))

product_name = "coffee"
(lambda x: print(x, "極品"))(product_name)

num = [100, 90, 80, 70]

ans = map(lambda x: x*2, num)
print(ans)
print(type(ans))
print(list(ans))

num = [100, 90, 80, 70]

for i in map(lambda x: x*2, num):
    print(i)

def discount(number):
    print("-"*10)
    return number *0.9

num = [100, 90, 80, 70]

for i in map(discount, num):
    print(i)

print(map(discount, num))
print(type(map(discount, num)))

def discount(number):
    print("-"*10)
    return number *0.9

num = [1000, 900, 800]
ite = iter(num)

for i in map(discount, num):
    print(i)


from functools import reduce

num = [100, 90, 80]
ans = reduce(lambda x, y: x+y, num)
print("ans:", ans)

num = [100, 90, 80]
ans = reduce(lambda x, y: x*y, num)
print("ans:", ans)

num = [100, 90, 80, 70, 60, 50]
ans = filter(lambda x:60 <= x <= 90, num)
print("ans:", ans)
print(list(ans))

from collections import Iterable

num = [100, 90, 80, 70, 60, 50]
ans = filter(lambda x:60 <= x <= 90, num)
print("Is Iterable", isinstance(ans, Iterable))
