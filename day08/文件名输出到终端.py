'''
编写一个程序将文件夹中的所有文件名输出到终端上
然后将py文件夹中的所有文件都改名为【传智播客】-python-07基础班。
'''

# 加载
import os

# 显示当前目录下的文件
list = os.listdir('./py')
for x in list:
    print(x)
