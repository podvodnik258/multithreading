import multiprocessing
import random
import time

def add_value(locker, array, index):
    with locker:
        num = random.randint(0, 20)
        vtime = time.ctime()
        array[index] = num
        print(f'array[{index}] = {num}, time = {vtime}')
        time.sleep(num)

arr = multiprocessing.Array('i', range(10))
lock = multiprocessing.Lock()
process = []

if __name__ == '__main__':
    for i in range(10):
        pr = multiprocessing.Process(target=add_value, args=(lock,arr,i,))
        process.append(pr)
        pr.start()


    for i in process:
        i.join()

    print(list(arr))


# ipython -i "2.2.1 Lock.py"
# lock.release() - ошибка.