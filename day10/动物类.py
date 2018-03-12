"""
创建一个动物类,
并通过__init__方法接受参数(name),
使用私有属性name保存参数值，并打印"init被调用".

在动物类中定义一个__del__()方法,
使其在删除的时候自动被调用,
并打印"del被调用".

使用动物类，实例化一个dog对象取名"八公"
"""


# 创建动物类
class Animal(object):

    # 初始化属性
    def __init__(self, name):
        self.__name = name
        print('init被调用')

    # 删除时调用
    def __del__(self):
        print('del被调用')


# 创建对象dog

dog = Animal('八公')
dog1 = dog
dog2 = dog

print('删除对象dog')
del dog

print('删除对象dog1')
del dog1

print('删除对象dog2')
del dog2

