import time
import threading

def get_data(data):
    print(f'[{threading.currentThread().name}] - {data}')
    time.sleep(5)


thr = threading.Thread(target=get_data, args=(str(time.time()),), name='thr-1')
thr.start()