"""
每一个文件一个进程
"""
import multiprocessing
import os, time, random


def copy_file(old_floder, new_floder, file_name, q):
    with open(old_floder + '/' + file_name, 'rb') as old_file:
        connect = old_file.read()

    with open(new_floder + '/' + file_name, 'wb') as new_file:
        new_file.write(connect)

    q.put(file_name)


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

    # 创建共用变量
    q = multiprocessing.Manager().Queue()

    # 创建进程
    po = multiprocessing.Pool(10)  # 创建１０个进程

    # 创建计数
    count = 0

    # 文件复制操作
    for file_name in file_list:
        # copy_file(old_floder, new_floder, file_name)
        po.apply_async(copy_file, (old_floder, new_floder, file_name, q))
        copyed_file = q.get()

        time.sleep(0.05)

        count += 1
        percent = count*100 / len(file_list)
        print('\r正在接收文件---　%s, 接收了　%.2f%%' % (copyed_file, percent), end='')



    # po.close()
    # po.join()

if __name__ == '__main__':
    main()
