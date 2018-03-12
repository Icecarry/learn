#coding=utf-8

'''
名片管理器v1.0 升级版，记录一张名片
* 使用个三个变量来记录用户输入的信息，包含姓名、电话、性别
* 姓名长度不是在6-20范围内，则提示错误
* 电话号码长度不是11，则提示错误
* 性别不是男或女，则提示错误
* 所有信息校验通过后，打印名片信息，程序结束
'''
while True:
    # 用户姓名
    name = input("请输入姓名(长度为 6 - 20)：")
    name_len = len(name)
    if name_len < 6 or name_len > 20:
        print("长度不对，请重输！")
    else:
        break

while True:
    # 用户电话
    tele = input("请输入电话号码（长度为11位）：")
    tele_len = len(tele)
    if len(tele) != 11:
        print("输入号码不是11位，请重输！")
    elif not tele.isdigit():
        print("输入的不是数字！")
    else:
        break

while True:
    # 用户性别
    sex = input("请输入性别（男或女）：")
    if sex != "男" and sex != "女":
        print("输入有误。请重新输入！")
    else:
        break


# 记录名片信息并打印
print("核对信息 ")
print("姓名：%s" % name)
print("性别：%s" % sex)
print("电话：%s" % tele)

