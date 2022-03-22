import threading
from multiprocessing import Pool
import os
import time


def get_drink(name, price):
    global global_name
    global_name = name
    print("PID:", os.getpid())
    time.sleep(3)
    print("名稱:{0}, 價格{1}".format(name, price))


def get_num():
    print("PID:", os.getpid(), end="\t")
    print("In get num:", global_name)
    time.sleep(2)


if __name__ == "__main__":
    start_time = time.time()
    data = {"coffee": 100, "tea": 90, "juice": 80}
    global global_name
    global process_1
    for i in data:
        process_1 = threading.Thread(target=get_drink, args=(i, data[i]))
        process_2 = threading.Thread(target=get_num, )
        process_1.start()
        process_2.start()

    else:
        process_1.join()
    end_time = time.time()
    print("total_time", end_time - start_time)
