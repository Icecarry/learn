"""
请写出一个Car基类,BMW类继承于Car类,
基类中有__init__方法(包含name,color)和run方法.
"""

# 汽车类
class Car(object):

    # 属性
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def run(self):
        print('在奔驰')


# 宝马类
class BMW(Car):


