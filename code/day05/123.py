#  2. 在桌面上编写一个py文件，完成以下功能要求
# # 1. 用多任务（多线程）的方式完成Test文件夹中的所有文件的复制
# # 2.
# # 新的文件夹的名字为“Test - 附件”   1.
# # 3.
# # 在复制文件的过程中，实时显示复制的进度    （用enu）
import threading
import os
import time


def file_copy():
    # file = os.mkdir("Test-附件")
    file_old = '/home/python/Desktop/Test'
    file_all = os.listdir(file_old)
    # print(file_all)
    length = len(file_all)
    for i in file_all:
        with open('/home/python/Desktop/Test' + '/' + i, 'r') as f:
            content = f.read()

        with open('/home/python/Desktop/Test-附件' + '/' + i, 'w') as f:
            f.write(content)
        time.sleep(0.3)
        length -= 1
        print("复制中--还有%d没有复制" % length)


# def file_build():
#     os.mkdir("Test-附件")


def main():
    # file_build()
    t = threading.Thread(target=file_copy)
    t.start()

    # while True:
    #     length = len(threading.enumerate())
    #     print("length:%d"%length)
    #     if length <= 1:
    #         break
    #
    #     time.sleep(1)

    # 找到文件


if __name__ == '__main__':
    main()
