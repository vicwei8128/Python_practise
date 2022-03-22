import threading
import os
import queue


def function_name():
    while True:
        print("PID", os.getpid())
        value = queue_obj.get()
        print("Do something {0}".format(value))
        queue_obj.task_done()


queue_obj = queue.Queue()
threading.Thread(target=function_name, daemon=True).start()
data = ["coffee", "tea", "juice", "milk", "water"]
for item in data:
    queue_obj.put(item)

queue_obj.join()
print("END")
