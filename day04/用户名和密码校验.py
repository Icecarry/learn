'''
用户名和密码格式校验程序
 要求从键盘输入用户名和密码
校验格式是否符合规则，用户名长度6-20，并且用户名必须以字母开头
 如果不符合，打印出不符合的原因，并再次提示输入
'''

#while 循环输入
while True:
    # 用户输入用户名和密码
    name = input("请输入用户名，长度为6 - 20，且要以字母开头：")
    pwd = input("请输入密码：")

    # 用户名长度6 - 20，字母开头
    length = len(name)
    if length < 6 or length > 20:
        print("用户名长度不够，请重输！")
    elif not name[0].isalpha():
        print("用户名没有以字母开头，请重输！")
    else:
        break