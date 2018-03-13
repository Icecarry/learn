"""
Queue　的使用方法
"""
import multiprocessing


def main():
    q = multiprocessing.Queue(3)  # 创建３个对象
    q.put('消息1')
    q.put('消息2')
    print(q.full())  # false
    q.put('消息3')
    print(q.full())  # true

    try:
        q.put('消息4', True, 2)
    except:
        print('消息队列已满，现有消息　%s' % q.qsize())

    try:
        q.put_nowait('消息4')
    except:
        print('消息队列已满，现有消息　%s' % q.qsize())

    # 先判断消息是否已满
    if not q.full():
        q.put_nowait('消息4')

    # 判断消息是否为空再读取
    if not q.empty():
        for i in range(q.qsize()):
            print(q.get_nowait())


if __name__ == '__main__':
    main()
