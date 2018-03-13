"""
给子进程传参数
"""
import os
import time
import multiprocessing


def run_proc(name, age, **kwargs):
    for i in range(10):
        print('子进程pid-----%s,name = %s, age = %s' % (os.getpid(), name, age))
        print('kwargs---')
        for item in kwargs.items():  # 遍历字典中的项
            print(item)

        time.sleep(0.2)


def main():
    # run_proc()
    p1 = multiprocessing.Process(target=run_proc, args=('test', 18), kwargs={'m': 20, 's': 66})
    p1.start()
    time.sleep(1)
    p1.terminate()
    p1.join()


if __name__ == '__main__':
    main()
