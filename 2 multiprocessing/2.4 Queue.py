import random
import multiprocessing
import time

def get_text(q):
    val = random.randint(0,5)
    q.put(str(val))


queue = multiprocessing.Queue()
pr_list = []

if __name__ == '__main__':
    for _ in range(10):
        pr = multiprocessing.Process(target=get_text, args=(queue,))
        pr_list.append(pr)
        pr.start()

    for i in pr_list:
        i.join()

    for elem in iter(queue.get, None):
        print(elem)
