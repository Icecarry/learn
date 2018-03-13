"""
进程间不共享全局变量
"""
import os
import time
import multiprocessing


num = [11,22]

def work1():
    """子进程代码"""
    print('子进程１pid－－－　%s' % os.getpid())
    for i in range(3):
        num.append(i)
        time.sleep(1)
        print('子进程１ %s 的num %s' % (os.getpid(), num))


def work2():
    """子进程２代码"""
    print('子进程２ %s 的num %s' % (os.getpid(), num))


def main():
    p1 = multiprocessing.Process(target=work1)
    p1.start()
    p1.join()

    p2 = multiprocessing.Process(target=work2)
    p2.start()
    p2.join()

if __name__ == '__main__':
    main()
