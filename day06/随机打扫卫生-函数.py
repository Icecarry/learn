"""
从键盘获取5个学生的名字，
然后随机抽出一名学生去打扫卫生
将存储学生名字的列表作为函数参数传入
"""

import random


def rand_name(name_list1):
    # 随机抽取名字
    num = random.randint(0, 4)
    # j = name_list[num]
    print("请 %s 同学去打扫。" % name_list1[num])


name_list = []
i = 0
while i < 5:
    # 获取5个名字
    name = input("请输入第 %d 个名字：" % (i + 1))
    name_list.append(name)
    i += 1
rand_name(name_list)


