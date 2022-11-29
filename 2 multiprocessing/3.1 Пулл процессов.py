import random
import multiprocessing
import time

def end_func(rasponce):
    print('end_func:', rasponce)

def out(x, y, z):
    print(f'value: {x}, {y}, {z}')
    return x, y, z

if __name__ == '__main__':
    with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p:
        p.starmap_async(out, [(1, 2, 3), (4, 5, 6)], callback=end_func)
        p.close()
        p.join()

