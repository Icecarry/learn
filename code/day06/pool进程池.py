"""
练习pool进程池的用法
"""
import multiprocessing
import os, time, random


def worker(num):
    t_start = time.time()
    print("%s 开始执行，进程号为 %s" % (num, os.getpid()))
    time.sleep(random.random())
    t_end = time.time()
    print('%s 执行结束，用时 %0.2f' % (num, (t_end - t_start)))


def main():
    po = multiprocessing.Pool(3)

    for i in range(0, 10):
        po.apply_async(worker, (i, ))

    print('-----start-----')
    po.close()
    po.join()
    print('-----end-----')


if __name__ == '__main__':
    main()
