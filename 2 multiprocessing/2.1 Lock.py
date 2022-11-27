import multiprocessing

lock = multiprocessing.Lock()

def get_value(l):
    l.acquire()
    pr_name = multiprocessing.current_process().name
    print(f'Процесс [{pr_name}] запущен')

if __name__ == '__main__':

    multiprocessing.Process(target=get_value, args=(lock,)).start()
    multiprocessing.Process(target=get_value, args=(lock,)).start()

# ipython -i "2.2.1 Lock.py"
# lock.release()