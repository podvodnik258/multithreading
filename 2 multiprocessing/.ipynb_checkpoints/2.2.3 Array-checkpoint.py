import multiprocessing

arr = multiprocessing.Array('i', range(10))
print(arr)

# ipython -i "2.2.1 Lock.py"
# lock.release() - ошибка.