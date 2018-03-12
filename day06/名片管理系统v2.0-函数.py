"""

名片管理器v2.0，管理多张名片，可以不断添加和查看名片
* 在上一版本的基础上，修改为使用[列表]来存储多张名片信息(注意阅读本题的提示信息)
* 可以打印名片内容的功能
* 可以清空名片内容的功能
"""


# 帮助信息
def print_help():
    # 选择操作
    print("=====================")
    print("功能帮助")
    print("1，增加一张名片")
    print("2，清空名片")
    print("3，退出")
    print("=====================")


# 打印功能函数
def print_card():
    for tmp in card_list:
        print(tmp)


# 添加名片函数
def add_card():
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

    # print("核对信息 ")
    # print("姓名：%s" % name)
    # print("性别：%s" % sex)
    # print("电话：%s" % tele)

    card = [name, tele, sex]
    card_list.append(card)
    print("注册成功")
    print_card()


# 清空函数
def clear_list():
    while True:
        length = len(card_list)
        if length > 0:
            card_list.pop()
        else:
            print("已经清空！")
            print_card()
            break


card_list = []

while True:
    print_help()
    cho = input("请选择功能：")
    if cho == '1':
        add_card()
    elif cho == '2':
        clear_list()
    elif cho == '3':
        break




