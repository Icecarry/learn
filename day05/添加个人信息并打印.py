"""
编程, 使用[字典]来存储一个人的信息（姓名、年龄、学号、QQ、微信、住址等），
这些信息来自键盘的输入，所有数据添加到字典后打印字典变量。
"""

# 用户信息输入
name = input('请输入姓名：')
age = input('请输入年龄：')
num = input('请输入学号：')
qq = input('请输入QQ：')
wechat = input('请输入微信：')
addr = input('请输入住址：')

# 定义空字典
info = {}

# 存入字典
info['name'] = name
info['age'] = age
info['num'] = num
info['qq'] = qq
info['wechat'] = wechat
info['addr'] = addr

for key,value in info.items():
    print('%s    %s' % (key, value))
