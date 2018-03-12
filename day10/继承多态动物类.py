"""
1. 创建一个动物的基类,其中有一个run方法
2. 创建一个Cat类继承于动物类
3. 创建一个Dog类继承于动物类
4. Cat类中不仅有run方法还有eat方法
5. Dog类中方法同上
6. 创建一个letRun函数，可以接收动物及其子类对象，并调用run方法
6. 编写测试代码以验证功能正常
"""


# 动物类
class Animal(object):
    def run(self):
        print('跑步')


class Cat(Animal):
    def eat(self):
        print('猫吃鱼')


class Dog(Animal):
    def eat(self):
        print('狗吃肉')


def letrun(animal):
    animal.run()

def leteat(animal):
    animal.eat()

letrun(Cat())
leteat(Cat())

letrun(Dog())
leteat(Dog())
