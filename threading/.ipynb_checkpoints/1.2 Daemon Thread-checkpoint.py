import time
import threading

def get_data(data):
    for _ in range(5):
        print(f'[{threading.currentThread().name}] - {data}')
        time.sleep(1)
        
thr = threading.Thread(target=get_data, args=(str(time.time()),))
thr.setDaemon(True)
thr.start()
#time.sleep(1)

print('finish')