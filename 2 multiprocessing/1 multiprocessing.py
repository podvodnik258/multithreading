import time
import multiprocessing

def test():
    for _ in range(3):
        print(f'{multiprocessing.current_process().name} - {time.time()}', 1)
        time.sleep(3)

if __name__ == '__main__':
    prc = []
    for _ in range(3):
        pr = multiprocessing.Process(target=test)
        prc.append(pr)
        pr.start()

    for i in prc:
        i.join()

    print('все процессы завершены')