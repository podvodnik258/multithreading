import time
import threading

def test():
    for _ in range(6):
        print('test')
        time.sleep(1)
        
thr = threading.Timer(5, test)
thr.setDaemon(True)
thr.start()

for _ in range(6):
    print('код продолжается..')
    time.sleep(1)

thr.cancel()
print('finish')