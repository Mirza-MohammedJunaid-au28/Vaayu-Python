import time
from threading import Thread
a = 0
def counter():
    global a

    for i in range(10000):
        a+=1
        time.sleep(0.2)

color_detection = Thread(target = counter)
color_detection.start()
time.sleep(5)
color_detection.join()
print("A : ",a)