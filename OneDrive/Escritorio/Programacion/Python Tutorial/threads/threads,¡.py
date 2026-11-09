import threading
import os, time

def worker(num):
    """thread worker function"""
    rand=ord(os.urandom(1))
    rand=str(rand)
    print ('Worker: %s ' % num + "random number: ", rand + "\n")
    return


for i in range(6):
    t = threading.Thread(target=worker, args=(i,))
   
    t.start()
    t.join()

