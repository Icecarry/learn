"""
使用threading模块中的Thread，
创建2个子线程，
线程1中每秒钟打印1个A，
线程2中每2秒钟打印1个B
"""
import threading
import time

def work1():
    while 1:
        print('A')
        time.sleep(1)

def work2():
    while 1:
        print('B')
        time.sleep(2)

def main():
    # 创建子线程
    t1 = threading.Thread(target=work1)

    t2 = threading.Thread(target=work2)

    # 执行子线程
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
