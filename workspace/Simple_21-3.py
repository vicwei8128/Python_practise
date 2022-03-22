from multiprocessing import Pool
import os
import time


def get_drink(name, price):
    print("PID:", os.getpid())
    time.sleep(3)
    print("名稱:{0}, 價格{1}".format(name, price))


if __name__ == "__main__":
    start_time = time.time()
    data = {"coffee": 100, "tea": 90, "juice": 80}
    with Pool(processes=3) as pool:
        for i in data:
            process_1 = pool.apply_async(get_drink, (i, data[i]))
        process_1.get()
    end_time = time.time()
    print("total_time", end_time - start_time)
