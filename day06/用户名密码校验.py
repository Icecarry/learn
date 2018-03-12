"""
用户名和密码格式校验程序:
    * 将键盘输入的数据作为函数参数传入
"""

# while True:

def path(name, pwd):
    # 用户名长度6 - 20，字母开头
    length = len(name)
    if length < 6 or length > 20:
        print("用户名长度不够，请重输！")
    elif not name[0].isalpha():
        print("用户名没有以字母开头，请重输！")
    else:
        # break
        pass


# 用户输入用户名和密码
name = input("请输入用户名，长度为6 - 20，且要以字母开头：")
pwd = input("请输入密码：")

path(name, pwd)
