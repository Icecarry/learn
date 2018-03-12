"""
练习__new__的使用

"""


class Func1(object):

    # 创建并返回实例对象，解释器自动调用
    def __new__(cls):
        print('__new__开始执行')
        obj = object.__new__(cls)
        print('对象创建中')
        # return obj

    def __init__(self):
        print('对象创建完成')

# Func1()
p1 = Func1()
print(p1)


