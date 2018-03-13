"""
每一个文件一个进程
"""
import multiprocessing
import os, time, random


def main():
    # 切换到桌面
    os.chdir('/home/python/Desktop/')

    # 旧文件夹名
    old_floder = input('请输入要复制的文件夹名：')

    # 创建新文件夹名
    new_floder = '[新]' + old_floder
    os.mkdir(new_floder)

    # 文件列表
    file_list = os.listdir(old_floder)

    # 文件复制操作
    for file_name in file_list:

        with open(old_floder + '/' + file_name, 'rb') as old_file:
            connect = old_file.read()

        with open(new_floder + '/' + file_name, 'wb') as new_file:
            new_file.write(connect)


if __name__ == '__main__':
    main()
