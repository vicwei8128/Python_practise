import os
import time
import multiprocessing as mp


def get_drink(name, price):
    print("PID:", os.getpid())
    time.sleep(3)
    print("名稱:{0}, 價格{1}".format(name, price))


if __name__ == "__main__":
    start_time = time.time()
    print("1.\tIn main PID:", os.getpid())
    data = {"coffee": 100, "tea": 90, "juice": 80}
    for i in data:
        process_1 = mp.Process(target=get_drink, args=(i, data[i]))
        process_1.start()
    end_time = time.time()
    print("2.\tIn main PID:", os.getpid())
    print("total_time", end_time - start_time)
