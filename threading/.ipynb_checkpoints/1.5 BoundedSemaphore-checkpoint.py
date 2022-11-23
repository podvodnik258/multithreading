import time
from threading import Thread, BoundedSemaphore

max_connections = 5
pool = BoundedSemaphore(value=max_connections)


def test():
    with pool:
        print(currentThread().name)
        time.sleep(6)
        
        
for i in range(10):
    Thread(target=test, name=f'thread-{i}').start