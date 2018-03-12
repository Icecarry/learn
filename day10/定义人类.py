"""
1. 定义一个人的基类,类中要有初始化方法,方法中初始化人的姓名,年龄.
2. 提供__str__方法，返回姓名和年龄信息
2. 将类中的姓名和年龄私有化.
3. 提供获取私有属性的方法.
4. 提供可以设置私有属性的方法.
5. 设置年龄时限制范围(0-100).
"""


class People(object):

    def __init__(self):
        self.__name = 'xp'
        self.__age = 1

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        if age >= 0 and age <= 100:
            self.__age = age
        else:
            print('输入的年龄不对。')
    def get_age(self):
        return self.__age

    def __str__(self):
        return '姓名： %s, 年领： %d' % (self.get_name(), self.get_age())


p1 = People()
p1.set_name('zx')
print(p1.get_name())
p1.set_age(4)
print(p1.get_age())
print(p1)

