import os
import time
print(time.localtime())

print("1.\t", time.localtime().tm_year)
print("2.\t", time.localtime().tm_hour)

time_a = time.time()
print("start time:", time_a)
time.sleep(5)
time_b = time.time()
print("end time:", time_b)

while True:
    print("執行扒網相關程式", time.time())
    time.sleep(5)

start_ALL = time.time()

start_a = time.time()
print("Do process A")
time.sleep(1.5)
end_a = time.time()
print("Process A track time:", end_a-start_a)

start_b = time.time()
print("Do process B")
time.sleep(2)
end_b = time.time()
print("Process B track time:", end_b-start_b)
end_All = time.time()
print("All process track time:", end_All - start_ALL)
