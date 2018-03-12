#coding:utf-8
# 名片管理系统：名片的增删改查
# 编写函数的总则：一个单独的功能就是一个单独的函数


def print_system_info():
    """打印系统提示信息"""
    print('=======================')
    print('欢迎使用 名片管理系统 v1.0')
    print('1.添加名片')
    print('2.删除名片')
    print('3.修改名片')
    print('4.查看名片')
    print('5.查看所有名字')
    print('0.退出系统')
    print('=======================')


def add_card():
    """添加一张名片"""
    # 3.1.1 获取新的信息
    new_name = input('请输入一个名字:')
    new_tel = input('请输入一个电话:')
    new_addr = input('请输入一个地址:')

    # 3.1.2 生成一个人信息的字典
    card = {}
    card['name'] = new_name
    card['tel'] = new_tel
    card['addr'] = new_addr

    # 3.1.2 保存信息到列表
    card_list.append(card)
    print('新的列表是: %s' % str(card_list))


def delete_card():
    """删除一张名片"""
    # 3.2.1 获取到要删除的名字
    delete_name = input('请输入要删除的名字:')

    # 3.2.2 从列表里把名字删除掉
    for card in card_list:
        if card['name'] == delete_name:
            card_list.remove(card)
            break
    else:
        print('没找到这个名字，无法删除')


def modify_card():
    """修改名片"""
    # 3.3.1 获取要修改的名字
    old_name = input('请输入要修改的名字:')

    # 3.3.2 获取新的名字
    new_name = input('请输入新的名字:')

    # 3.3.3 替换旧名字为新名字
    for card in card_list:
        if card['name'] == old_name:
            card['name'] = new_name
            break
    else:
        print('没找到这个名字，无法修改')


def find_card():
    """查找一张名片"""
    # 3.4.1 获取要查找的名字
    find_name = input('请输入要查找的名字:')

    # 3.4.2 判断名字是否存在
    for card in card_list:
        if card['name'] == find_name:
            print('找到了')
            break
    else:
        print('没找到')


def show_all_card():
    """打印所有名片"""
    for card in card_list:  # card = {'name': 'zs', 'tel': '110', 'addr': 'aaa'}
        print('姓名: %s    电话：%s     地址:%s' % (card['name'], card['tel'], card['addr']))


def main():

    while True:
        # 1. 打印系统信息
        print_system_info()

        # 2. 获取用户选择的操作
        command = input('请输入要执行操作的数字：')

        # 3. 根据用户选择执行不同的操作
        if command == '1':
            # 添加
            add_card()

        elif command == '2':
            # 删除
            delete_card()

        elif command == '3':
            # 修改
            modify_card()

        elif command == '4':
            # 查看一张名片
            find_card()

        elif command == '5':
            # 查看所有
            show_all_card()

        elif command == '0':
            # 退出
            break

        else:
            # 不知道用户输入了什么
            print('选择错误，无法处理的指令: %s' % command)


card_list = []  # 存放名字的列表，需要放在循环外

# 从文件读取数据，添加到列表里
# 打开
data_file = open('card.dat', 'r')

# 读取
content = data_file.read()
old_cards = eval(content)  # 使用 eval 把字符串当作代码来执行，获取到列表数据

# 把文件里的名片添加到列表里
card_list.extend(old_cards)
# print(card_list)

# 关闭
data_file.close()

# 程序运行中
main()

# 退出程序时，保存名片数据到文件
# 打开
save_file = open('card.dat', 'w')  # 擦除原有数据，重新保存

# 保存
save_file.write(str(card_list))  # 把列表转换成字符串保存

# 关闭
save_file.close()

