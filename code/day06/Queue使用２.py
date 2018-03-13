"""
两个方法，一个写，一个读
"""
from multiprocessing import Process, Queue
import os, time, random


# 写进程代码
def write(q):
    ls = ['A', 'B', 'C']
    print('进程１－－－　%s' % os.getpid())
    for i in ls:
        print("正在发送 %s ..." % i)
        q.put(i)
        time.sleep(random.random())


# 读进程代码
def read(q):
    print('进程２－－－　%s' % os.getpid())
    while True:
        if not q.empty():
            value = q.get(True)
            print('正在获取数据　%s' % value)
            time.sleep(random.random())
        else:
            break


if __name__ == '__main__':
    print('主进程－－－　%s' % os.getpid())
    q = Queue()

    qw = Process(target=write, args=(q,))
    qr = Process(target=read, args=(q,))

    qw.start()
    qw.join()

    qr.start()
    qr.join()

    print('')
    print("程序结束")
