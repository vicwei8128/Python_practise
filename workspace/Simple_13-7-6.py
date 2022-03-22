def function(x):
    while True:
        yield x
        x += 1
n = function(0)

print(next(n))
print(next(n))
print(next(n))
