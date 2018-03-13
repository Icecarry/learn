"""
1. 用多任务（多线程）的方式完成Test文件夹中的所有文件的复制
2. 新的文件夹的名字为“Test-附件”
3. 在复制文件的过程中，实时显示复制的进度
"""
import os
import threading
import time


def copy_file():
    # 获取文件目录
    list_file = os.listdir('./Test')
    # 循环取出文件
    for file in list_file:
        print('正在复制文件: %s ...' % file)
        # file_source = open(file, 'r')
        # file_copy = open('./Test-附件' + file, 'w')
        with open('./Test/'+file, 'r') as file_source:
            file_source_read = file_source.read()

        with open('./Test-附件/'+file, 'w') as file_copy:
            file_copy.write(file_source_read)

            # file_source.close()
            # file_copy.close()
        time.sleep(0.05)


def main():
    os.chdir('/home/python/Desktop')
    os.mkdir('./Test-附件')
    # 调用copy_file
    t1 = threading.Thread(target=copy_file)
    # copy_file()
    t1.start()

if __name__ == '__main__':
    main()
