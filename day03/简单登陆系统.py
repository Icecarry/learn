'''
从键盘输入一个用户名和密码，判断是否正确，
如果是则打印登录系统成功，
否则显示用户名或密码错误
'''

#请求用户输入
acc = input("请输入账号：")
pwd = input('请输入密码：')

#判断账号密码是否匹配
real_acc = "xiaoming"
real_pwd = "123456"

if acc == real_acc and pwd == real_pwd:
    print("登陆成功！")
else:
    print("用户民或密码错误！")