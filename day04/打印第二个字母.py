'''
从键盘中输入5个学生的名字，存储到列表中，
然后打印出每个学生名字中的第2个字母
'''

#输入5次
i = 0
name_list = []
while i < 5:

    # 输入名字
    name = input("请输入第 %d 名字：" % (i + 1))
    name_list.append(name)

    i += 1
# print(name_list)

# print(name_list[3][2])
for tmp in name_list:
    print(tmp[1])