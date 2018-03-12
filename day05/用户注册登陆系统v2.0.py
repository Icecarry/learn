'''
 用户注册登录系统V2.0
设计一个程序
要求用户可以实现登录、注册、注销登录等功能
用户的用户名(长度6-20)、密码(长度8-20)、昵称、年龄信息保存到字典中
将每个已注册用户的保存到列表中，即将上一步的字典保存到列表中
维护用户的登录状态，每次只能有一个用户处于登录状态，直到选择注销登录
如果不选择退出系统，该程序应当一直运行
'''


# 存放信息的列表
sys_list = []

# 记录登陆信息变量
loginUser = '0'

while True:
    # 打印帮助信息
    print("================")
    print("1,注册")
    print("2,登陆")
    print("3,注销登陆")
    print("4,退出")
    print("================")

    num = input("请输入选择：")

    # 功能注册
    # 循环输入员工信息
    # 用户信息输入
    if num == '1':
        while True:
            info = {'用户名': '', '密码': '', '昵称': '', '年龄': ''}
            # 修改字典键值
            name = input("请输入用户名：")
            if 6 <= len(name) <= 20:
                info['用户名'] = name
            else:
                print("用户名输入有误！重输！")
                continue

            pwd = input("请输入密码：")
            if 8 <= len(pwd) <= 20:
                info['密码'] = pwd
            else:
                print("密码输入有误，请重输！")
                continue

            nc_name = input("请输入昵称：")
            info['昵称'] = nc_name

            age = input("请输入年龄：")
            info['年龄'] = age

            sys_list.append(info)
            break

    # 功能登陆
    # 用户输入账号，和密码，与列表里的字典匹配
    if num == '2':
        login_name = input('请输入账号：')
        login_pwd = input('请输入密码：')

        if loginUser == '1':
            print('已有用户登陆，请不要重复登陆！')
        elif len(sys_list) == 0:
            print('不存在')
        else:
            for tmp in sys_list:
                if login_name == tmp['用户名']:
                    if login_pwd == tmp['密码']:
                        loginUser = '1'
                        print('登陆成功')
                        break
                    else:
                        print('账号或密码输入有误请重新登陆。')
                        break
                # else:
            else:
                print('账号输入有误请重新登陆。')
                    # break

    # 功能注销登陆
    if num == '3':
        loginUser == '0'
        print('注销成功')

    # 功能退出
    if num == '4':
        print(sys_list)
        break

