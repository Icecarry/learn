"""
进程池中的Queue
"""
import multiprocessing
import os, time, random


def write(q):
    print('%s write子进程，父进程　%s' % (os.getpid(), os.getppid()))
    for i in range(0, 10):
        q.put(i)


def read(q):
    print('%s 子进程，父进程　%s' % (os.getpid(), os.getppid()))
    for i in range(q.qsize()):
        print('接收到数据： %s' % q.get(True))


def main():
    print("---start----,进程 (%s)" % os.getpid())
    q = multiprocessing.Manager().Queue()
    po = multiprocessing.Pool()

    po.apply_async(write,(q,))

    time.sleep(1)

    po.apply_async(read,(q,))


    po.close()
    po.join()

    print('---end----,进程 (%s)' % os.getpid())



if __name__ == '__main__':
    main()
