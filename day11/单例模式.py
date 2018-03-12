# """
# 测试单例模式
# """
#
#
class People(object):
    item = None
    creat_naem = True

    def __new__(cls, name):
        if not cls.item:
            cls.item = object.__new__(cls)
        return cls.item

    def __init__(self, name):
        if self.creat_naem:
            self.name = name
            self.creat_naem = False
            # print('创建 %s' % name)

    def __str__(self):
        return '创建 %s' % self.name


p1 = People('zs')
print(p1)

p2 = People('ls')
print(p2)


# class Person(object):
#
#     instance = None  # 类属性
#     is_first_run = True
#
#     def __new__(cls, *args, **kwargs):
#         if cls.instance == None:  # 当 instance 为 None 才创建新对象
#             cls.instance = object.__new__(cls)
#
#         return cls.instance
#
#     def __init__(self, name):
#         if Person.is_first_run:  # 单例模式，只应该在第一次创建对象的时候初始化属性
#             self.name = name
#             Person.is_first_run = False  # 修改标记
#
#     def set_name(self, new_name):
#         self.name = new_name
#
# p1 = Person('张三')
# print(p1.name)
# p2 = Person('李四')
# print(p2.name)
#
# print(p1.name)
