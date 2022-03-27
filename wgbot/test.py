import threading
import time

def vk():
    i = 20000000
    for x in range(0,i):
        print ("A")
        time.sleep(2)


def update_tokens():
    i = 20000000
    for x in range(0,i):
        print ("B")
        time.sleep(2)

th1 = threading.Thread(target=vk)
th2 = threading.Thread(target=update_tokens)

for i in range(0,1):
    print("sdf")
    th1.start()
    th2.start()