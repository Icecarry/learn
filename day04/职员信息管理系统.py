'''
职员信息管理系统
    * 使用列表来记录多个员工的信息
    * 要求依次从键盘录入每位员工的信息，
    并使用字典来保存，
    包括姓名、员工id、出生年月、籍贯、身份证号、入职时间
    * 要求能随时查看已录入的员工信息
'''

# 空列表存放字典
employee = []

# 循环输入员工信息
while True:
    print("================")
    print("1,输入员工信息")
    print("2,录入完毕退出")
    print("3,输出员工信息")
    print("================")

    num = input("请输入选择：")
    if num == '1':
        # 定义员工信息
        info = {'姓名': 'none', '员工id': 'none', '出生年月': 'none', '籍贯': 'none', '身份证号': 'none', '入职时间': 'none'}

        # 修改字典键值
        name = input("请输入姓名：")
        info['姓名'] = name

        yg_id = input("请输入员工id：")
        info['员工id'] = yg_id

        birth = input("请输入出生年月：")
        info['出生年月'] = birth

        place = input("请输入籍贯：")
        info['籍贯'] = birth

        sfz_id = input("请输入身份证号：")
        info['身份证号'] = birth

        time = input("请输入入职时间：")
        info['入职时间'] = birth

        # 存入列表
        employee.append(info)
    elif num == '2':
        break
    elif num == '3':
        for x in employee:
            print(x)





