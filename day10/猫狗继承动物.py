"""
1. 动物:吃,喝,跑,玩
2. 猫:喵喵叫
3. 狗:旺旺叫
4. 猫、狗继承于动物,并且有2、3中自己的方法.
5. 创建猫和狗的对象，并调用可用的所有方法
"""


# 创建动物类
class Animal(object):

    def eat(self):
        print('吃')

    def drink(self):
        print('喝')

    def run(self):
        print('跑')

    def play(self):
        print('玩')



class Cat(Animal):

    def shout(self):
        print('喵喵叫')


class Dog(Animal):
    def shout(self):
        print('汪汪叫')

mao = Cat()
mao.eat()
mao.drink()
mao.run()
mao.play()
mao.shout()

gou = Dog()
gou.eat()
gou.drink()
gou.run()
gou.play()
gou.shout()

