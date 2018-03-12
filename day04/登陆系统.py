'''
编写代码模拟用户登陆。
要求：用户名为 python，密码 123456，
如果输入正确，打印“欢迎光临”，程序结束，
如果输入错误，提示用户输入错误并重新输入。
'''



#判断账号密码是否匹配
real_acc = "python"
real_pwd = "123456"

while True:
    #请求用户输入
    acc = input("请输入账号：")
    pwd = input('请输入密码：')

    if acc == real_acc and pwd == real_pwd:
        print("欢迎光临！")
        break
    else:
        print("用户民或密码错误！请重新输入！")
        # continue
# if acc == real_acc and pwd == real_pwd:
#     print("欢迎光临！")
# else:
#     print("用户民或密码错误！")