"""
定义一个类，
提供可以重新设置私有属性name的方法，
限制条件为字符串长度小于10,才可以修改.
"""


class People(object):

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if len(name) < 10:
            self.__name = name
        else:
            print('字符过长')


p1 = People('ren')
p1.set_name('assssaasdadadasd')
print(p1.get_name())

