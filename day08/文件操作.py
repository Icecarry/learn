# 文件复制

import os

# 指定要复制的文件的名字
old_file = input('请输入要复制的文件名：')

# 输入字符切割
num = old_file.rfind('.')
copy_file = old_file[:num] + '(复制)' + old_file[num:]

# 打开文件
f = open(old_file, 'r')
c = open(copy_file, 'w')
# 读取文件
while True:
    stt = f.read(8*1024)
    if len(stt) != 0:
        c.write(stt)
    else:
        break
# con = f.read()
# c.write(con)

# 关闭文件
f.close()
c.close()

