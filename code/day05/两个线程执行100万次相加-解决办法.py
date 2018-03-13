"""
创建2个子线程，
线程1、2同时对全局变量num各加100万次操作（num初始值为0），
每次加1，最后执行完成打印结果
"""
import threading


def work1():
    global num
    for i in range(1000000):
        loc.acquire()
        num += 1
        loc.release()
    print('t1', num)

def work2():
    global num
    for i in range(1000000):
        loc.acquire()
        num += 1
        loc.release()
    print('t2', num)

def main():
    t1 = threading.Thread(target=work1)

    t2 = threading.Thread(target=work2)

    t1.start()
    t2.start()

num = 0
loc = threading.Lock()

if __name__ == '__main__':
    main()
