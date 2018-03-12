'''
编写一段代码以完成文件的备份

**要求：**

1. 创建python07基础班文件夹

2. 在文件夹中创建gailun.txt文件

3. 打开文件在gailun.txt中写入"德玛西亚！人在塔在！"，并关闭文件

4. 读取文件内容，将输入的数据输出到屏幕上，并关闭文件

5. 在文件夹中创建gailun副本.txt文件

6. 读取gailun.txt文件中的数据，写入gailun副本.txt文件中，并关闭两个文件

7. 打开副本文件，查看文件中是否有内容

**提示：**

1. 文件的操作流程打开文件，写入/读取数据，关闭文件
'''


import os

# 创建文件夹
os.mkdir('python07基础班')
os.chdir('./python07基础班')

# 创建文件
f = open('gailun.txt', 'w')

# 写入
f.write('de ma xi ya ! ren zai ta zai!')

# 关闭
f.close()

# 读取文件内容输出到屏幕上
f2 = open('gailun.txt', 'r')
read_data = f2.read()
print(read_data)
f2.close()

# 创建副本，传数据
f3 = open('gailun副本.txt', 'w')
f4 = open('gailun.txt')

tmp = f4.read()
f3.write(tmp)

f3.close()
f4.close()

# 打印
f5 = open('gailun副本.txt',)
tmp1 = f5.read()
print(tmp1)
f5.close()
