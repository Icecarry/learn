from multiprocessing import Process
import time


def run_proc():
    """ 子进程要执行的代码"""
    while 1:
        print('-----2-----')
        time.sleep(1)


def main():
    # 调用while 循环
    # run_proc()
    p1 = Process(target=run_proc)
    p1.start()
    while 1:
        print('-----1-----')
        time.sleep(1)


if __name__ == '__main__':
    main()
